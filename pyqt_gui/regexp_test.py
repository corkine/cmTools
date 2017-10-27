#! /usr/bin/env python3
'''
这是我在学习PyQt和正则表达式的时候写的一个小程序，其主要被设计用来查看系统目录下的文件，同时对其应用正则表达式进行筛选。这个程序最大的特点就是及时窗口，输入任何正则规则，程序会自动回传数据进行及时显示。
Write by Corkine Ma (cm@marvinstudio.cn)
'''
try:
    import PyQt5,sys,os,re
    from tkinter import Tk
    from tkinter.messagebox import showwarning
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
except Exception as _err:
    Tk().withdraw()
    warn3=showwarning('WARNING','检测到有组件尚未导入，请检查后再试。\n错误详情：%s'%_err)
    warn3


class Form1(QDialog):
    def __init__(self,parent=None):
        super(Form1,self).__init__(parent)

        self.address=os.getcwd()
        self.outputdir=[]
        self.inputdir=[]
        self.setWindowTitle("Python RE Module Test")
        # self.okbutton=QPushButton("&GO!")
        label1=QLabel("The Folder List Files")
        label2=QLabel("The Result with your RERules choose Files")
        label_b=QLabel("\n")
        self.inputline=QLineEdit("\w+")
        self.inputaddress=QLineEdit(self.address)
        self.folder_in=QListWidget()
        self.folder_out=QListWidget()
        self.rebutton=QPushButton("&Find!")
        self.selectfolder=QPushButton("&Select")
        layout_a=QHBoxLayout()
        layout_a.addWidget(self.inputaddress)
        layout_a.addWidget(self.selectfolder)
        # layout_a.addWidget(self.okbutton)
        layout_b=QHBoxLayout()
        layout_b.addWidget(self.inputline)
        layout_b.addWidget(self.rebutton)
        layout=QVBoxLayout()
        layout_f=QHBoxLayout()
        layout_f1=QVBoxLayout()
        layout_f1.addWidget(label1)
        layout_f1.addWidget(self.folder_in)
        layout_f2=QVBoxLayout()
        layout_f2.addWidget(label2)
        layout_f2.addWidget(self.folder_out)
        layout_f.addLayout(layout_f1)
        layout_f.addLayout(layout_f2)
        layout.addLayout(layout_a)
        layout.addLayout(layout_b)
        layout.addLayout(layout_f)
        self.setLayout(layout)
        
        # self.okbutton.clicked.connect(self.gotoaddress)
        self.inputaddress.setFocus()
        self.inputaddress.selectAll()
        self.rebutton.clicked.connect(self.checkrules)
        self.inputline.textEdited.connect(self.checkrules)
        self.selectfolder.clicked.connect(self.choosefolder)
        self.selectfolder.clicked.connect(self.checkrules)
        self.inputaddress.textEdited.connect(self.checkrules)
        
    changecwd=pyqtSignal(str)

    def choosefolder(self):
        dlg_2=QFileDialog.getExistingDirectory(self,"Choos CWD",self.address,QFileDialog.ShowDirsOnly)
        if dlg_2 and dlg_2 != self.address:
            self.address=str(dlg_2)
            self.inputaddress.setText(self.address)
            self.update_UI()

    # def gotoaddress(self):
    #     try:
    #         address=str(self.inputaddress.text())
    #         if address != '' and address != " ":
    #             self.address=address
    #             self.update_UI()
    #     except Exception as _err:
    #         QInputDialog.getText(self,"gotoaddress警告","出现错误\n错误原因:%s"%_err)
    #         pass

    def checkrules(self):
        try:
            self.rule=str(self.inputline.text())
            outputdir=self.outputdir
            self.address=str(self.inputaddress.text())
            try:
                left_=right_=0
                if self.rule != None and self.rule !=' ' and self.rule !='\\' and self.rule[-1:] !='\\' and self.rule[-1:] !='[' and self.rule[-1:] !='!':
                    for x in self.rule:
                        if x =="[":
                            left_+=1
                        elif x =="]":
                            right_+=1
                    if left_ != right_:
                        self.rule="\w+"
                    else:pass
                    result_ = self.runcheck(self.rule,self.address)
                    self.outputdir=result_
                    self.update_UI()
            except Exception as _err:
                # QInputDialog.getText(self,'checkrules1提示',"错误：%s"%_err)
                pass
        except Exception as _err:
                # QInputDialog.getText(self,'checkrules2提示',"错误：%s"%_err)
                pass

    def runcheck(self,rule_='',address_=''):
        try:
            reobj=re.compile(rule_)
            result_=[]
            for file in os.listdir(address_):
                result=reobj.search(file)
                if result:
                    result_.append(file)
                    # QInputDialog.getText(self,'runcheck提示',"错误：%s"%file)
                    pass
            return result_
        except Exception as _err:
            # QInputDialog.getText(self,'runcheck提示2',"错误：%s"%_err)
            pass

    def update_UI(self):
        self.inputdir=os.listdir(self.address)
        try:
            self.folder_in.clear()
            self.folder_out.clear()
            try:
                self.folder_out.addItems(self.outputdir)
            except:
                pass
        except Exception as _err:
            QInputDialog.getText(self,'update提示',"错误：%s"%_err)
            pass

        for findfile in self.inputdir:
            if findfile in self.outputdir:  
                QListWidgetItem(findfile,self.folder_in).setForeground(QColor(200,111,100))
            else:
                QListWidgetItem(findfile,self.folder_in)
            

if __name__=="__main__":
    
    app=QApplication(sys.argv)
    form=Form1()
    form.show()
    app.exec_()
    
    