#!/usr/bin/env python3

__author__='TroubleMaker'
__version__='9.9.9'

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ui_fakedlg
import fakefunc

class Form(QDialog,ui_fakedlg.Ui_fakeData):
    

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.selectFile)
        self.pushButton_2.clicked.connect(self.runFake)
        self.inputfile=''
        self.howmuch=100
    
    def selectFile(self):
        self.label.setText("")
        filename,filetype = QFileDialog.getOpenFileName(self,"选择TXT格式数据文件")
        if not filename=='':
            if filename[-4:] == '.txt':
                self.inputfile=filename
                self.label.setText("已选择文件，点击开始继续")
            else:
                self.label.setText("选取文件出错：请选取一个txt格式数据文件")
        else:
            self.label.setText("选取文件出错")

    def runFake(self):
        error_info = ''
        howmuch, ok= QInputDialog.getText(self,"提示 - 数据量","你想要多少数据？请输入一个合适的整数")
        sex_howmuch, sex_ok= QInputDialog.getText(self,"提示 - 性别比","请输入需要声称的数据的性别比例？\n比如男女比1：2请输入整数12[最大99]")
        age_howmuch, age_ok= QInputDialog.getText(self,"提示 - 年龄范围","请输入你希望生成的数据的年龄特征范围。\n比如20-30岁可以输入 20空格30\n注意：包括20和30岁，随机取整数")
        data_howmuch, data_ok= QInputDialog.getText(self,"提示 - 数据偏移","数据偏移设置\n系统会自动根据已有数据偏移-1，0，1，输入一个三位数整数，比如131表示偏移-1，0，1的比例为1：3：1")
        try:
            howmuch = str(howmuch)
            self.howmuch = int(howmuch)
            if int(sex_howmuch) > 99 or int(sex_howmuch) < 11:
                raise ValueError("性别比例数据错误")
            sex_howmuch = str(sex_howmuch)
            data_howmuch = str(data_howmuch)
            age_howmuch_tuple = age_howmuch.split(" ")[0],age_howmuch.split(" ")[1]
            result,info=fakefunc.Fake_201942(self.inputfile,self.howmuch,data_random=data_howmuch,sex_random=sex_howmuch,age_random=age_howmuch_tuple)
            (a,b,c)=howmuch,str(sex_howmuch[0])+':'+str(sex_howmuch[1]),str(str(age_howmuch.split(" ")[0])+'岁到'+str(age_howmuch.split(" ")[1])+'岁')
        except:
            error_info = "读取设置出错，将按照默认输出100被试的数据, 偏移比为1:7:1, 男女性别比为1：3"
            result,info=fakefunc.Fake_201942(self.inputfile)
            a,b,c='100','1:3','20-30岁'
        if error_info =='':
            self.label.setText("[%s份数据,性别比为%s,年龄范围为%s]"%(a,b,c)+info)
        else:
            self.label.setText("%s\n[%s份数据,性别比为%s,年龄范围为%s]"%(error_info,a,b,c)+info)

    def updateStatus(self):
        pass







app = QApplication(sys.argv)
form=Form()
form.show()
app.exec_()
        