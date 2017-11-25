#!/usr/bin/env python3

import sys,os,io,shelve,traceback
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ui_setting

class Form(QDialog,ui_setting.Ui_Dialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.selectDb)
        self.pushButton_2.clicked.connect(self.selectCWD)
        # self.pushButton_4.clicked.connect(self.selectAlert)
        self.address=''
        self.dbaddress =''
        # self.alertaddress = ''
        self.buttonBox.accepted.connect(self.saveIt)
        
        try:
            loadfile = open('daily.setting','r')
            thefile = loadfile.read()
            # print(thefile)
            self.address=str(thefile.split(",")[0])
            self.dbaddress=str(thefile.split(",")[1])
            # self.alertaddress = str(thefile.split(",")[4])
            self.label_3.setText(self.dbaddress)
            self.label_4.setText(self.address)
            self.lineEdit.setText(str(thefile.split(",")[2]))
            self.lineEdit_2.setText(str(thefile.split(",")[3]))
            # self.label_5.setText(self.alertaddress)
        except:
            QMessageBox.warning(self,"WARN",'从之前的文件中读取出错，如果你第一次使用此程序，请忽略此条消息')


    def selectCWD(self):
        address=QFileDialog.getExistingDirectory(self,"选择需要监视的文件夹",os.getcwd(),QFileDialog.ShowDirsOnly)
        if address != None:
            self.address = address
            self.label_4.setText(self.address)
        else:
            self.label_4.setText('未选择')

    def selectDb(self):
        choose = QMessageBox.information(self,'选项',"你是否需要新建一个数据库文件？如果没有，请点击'OK',否则点击'Cancel'选择你的数据库问卷",QMessageBox.Ok|QMessageBox.Cancel)
        if choose == QMessageBox.Ok:
            address=QFileDialog.getExistingDirectory(self,"选择需要监视的文件夹",os.getcwd(),QFileDialog.ShowDirsOnly)
            db=shelve.open(address+'/mydailydata')
            db['1999年1月1日.docx']='Update at NOTIME'
            self.dbaddress = address+'/mydailydata'
            self.label_3.setText(self.dbaddress)
        else:
            filename,type = QFileDialog.getOpenFileName(self,"选择你的数据库文件",'',"cmData files (*.dat)")
            # print(filename)
            if filename != None:
                if '.bak' in filename[-4:] or '.dat' in filename[-4:] or '.dir' in filename[-4:]:
                    filename = filename[:-4]
                    self.dbaddress = filename
                    self.label_3.setText(self.dbaddress)
                    # print(self.dbaddress)
                else:
                    self.label_3.setText('未选择')
                    QMessageBox.warning(self,"WARN",'无效文件，请重新选取')

    # def selectAlert(self):
    #     filename,type = QFileDialog.getOpenFileName(self,"选择你的提醒程序",'',"cmEXE files (*.exe)")
    #     if filename != None:
    #         self.alertaddress = filename
    #         self.label_5.setText(self.alertaddress)
            
    def saveIt(self):
        emailaddress = str(self.lineEdit.text())
        regularexp = str(self.lineEdit_2.text())
        if emailaddress == '' or regularexp == '' or self.dbaddress =='' or self.address == '' :#不对提醒程序判断
            QMessageBox.warning(self,"WARN",'输入数据无效，请检查后再试')
        else:
            try:
                # print(emailaddress,regularexp,self.address,self.dbaddress,self.alertaddress)
                savedata = open('daily.setting','w')
                savedata.write('%s,%s,%s,%s'%(self.address,self.dbaddress,emailaddress,regularexp))
                savedata.close()
                QMessageBox.information(self,"Info",'设置数据保存在daily.setting文件中')
                # print(os.getcwd())
            except Exception as _err:
                print(traceback.format_exc())
                QMessageBox.warning(self,"WARN",'数据保存失败')
                # print(os.getcwd())
        
    def runTest(self):
        pass        
        # os.startfile(r"C:\Users\Administrator\计划任务\EveryDayNotice.exe")


if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Daily Notice")
    app.setOrganizationName("Marvin Studio")
    app.setOrganizationDomain("http://www.marvinstudio.cn")
    form = Form()
    form.show()
    app.exec_()