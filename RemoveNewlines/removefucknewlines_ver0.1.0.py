#!/usr/bin/env python3
import sys
import PyQt5
# from PyQt5.QtCore import 
from PyQt5.QtGui import QClipboard,QGuiApplication
from PyQt5.QtWidgets import QDialog,QApplication,QPushButton,QTextBrowser,QVBoxLayout,QHBoxLayout,QMessageBox
__TITLE__ = '论文复制行间断去除'
__VERSION__ = "0.5.1"
class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.info_label = '请将需要处理的文本复制到剪贴板'
        self.info_label2 = QPushButton("使用帮助")
        self.info_label3 = QPushButton("关于本程序")
        self.setWindowTitle("%s %s - %s"%(__TITLE__,__VERSION__,self.info_label))
        self.resize(800,600)
        self.beforedoit = ''
        self.textbrowser = QTextBrowser()
        self.setWhatsThis("这是一个快速移除空格的小程序")
        layout = QVBoxLayout()
        layout_child = QHBoxLayout()
        layout_child.addStretch()
        layout_child.addWidget(self.info_label2)
        layout_child.addWidget(self.info_label3)
        
        layout.addWidget(self.textbrowser)
        layout.addLayout(layout_child)
        self.setLayout(layout)

        self.info_label2.clicked.connect(self.showHelp)
        self.info_label3.clicked.connect(self.showAbout)

    def enterEvent(self, event = None):
        # print("SHOW!")
        clipboard=QGuiApplication.clipboard()
        try:
            self.beforedoit = clipboard.text()
            self.beforedoit = self.beforedoit.replace('\n',' ')
            self.info_label = '处理完毕，更新后的文本已复制到你的剪贴板'
            clipboard.setText(self.beforedoit)
        except:
            self.info_label = '[未检测到内容]请将需要处理的文本复制到剪贴板'
            
        self.textbrowser.setText(self.beforedoit)
        self.setWindowTitle("%s %s - %s"%(__TITLE__,__VERSION__,self.info_label))

    # def contextMenuEvent(self, event):
    #     menu = QMenu()
    #     action1 = menu.addAction("使用说明")
    #     action2 = menu.addAction("关于本软件")
    #     menu.exec_(event.globalPos())

    def showHelp(self):
        QMessageBox.about(self,"使用帮助","""
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">本文档适用于版本 0.0.1，当前软件版本为 %s</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; text-decoration: underline;">简要介绍：</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">本程序可以快速去除给定文本的“\\n”标识符。</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; text-decoration: underline;">本程序希望解决以下问题：</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">当代文献排版都是左右两栏，我们获取的电子版文献（可能你是从百度或者Google学术下载的）一般都可以复制文字，但是这些复制过的文字存在断行问题，原本就是一行的文字经过这样直接复制后粘贴到别的地方，比如Word中会出现非常麻烦的断行。这件事情很麻烦，因为当我们复制过去后需要手动去调整让这些断行变得整齐，因此有了本程序。</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">这个问题很好解决，只需要使用Python的replace()函数就好，不过，为了处理一段文本，还需要执行一段代码，然后把文本粘贴进去、复制出来，麻烦程度不亚于手动处理。</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; text-decoration: underline;">使用说明：</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">得益于Qt强大的工具集和Python的快速编程能力，你只用在Acrobat等PDF阅读器中选定一些文本，然后返回本程序，只要鼠标停留在本界面的任何位置即可（甚至不需要滑动，只要鼠标在窗口上就行），（其实你可以让这个窗口大一点，切换回来的时候自然鼠标就在窗口上面，什么都不用做），然后打开你的Word，直接粘贴即可，当激活本程序窗口时，行之间的间断会自动去除。一个我期望的工作流是：在阅读器中按下Ctrl+C复制文本，按下Alt+Table切换到本程序，然后继续按下Alt+Table切换到Word等你需要粘贴的地方就好。       </p></body></html> 
        
        """%(__VERSION__))
        
    def showAbout(self):
        QMessageBox.about(self,"CM LOVE Python","""
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">%s version %s</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Written by <span style=" font-weight:600;">Corkine Ma</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Email:cm@marvinstudio.cn</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">本程序使用 Python 和 Qt 开发，程序遵循GPL v2开源协议，你可以在http://tools.mazhangjing.com 此网站找到程序的源代码，如果没有，请联系作者。</p></body></html>
        
        
        
        """%(__TITLE__,__VERSION__)
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()