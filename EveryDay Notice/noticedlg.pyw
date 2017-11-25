#!/usr/bin/env python3

import sys,time
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import UI_noticedlg
import appsetting

__VERSION__ = '0.2.0'

StyleSheet="""
QLabel#label_num{
    color:red;
}

"""
class Form(QDialog,UI_noticedlg.Ui_Dialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setupUi(self)
        self.starttime=time.ctime()
        self.label_num.setText(" 1")
        self.setStyleSheet(StyleSheet)
        self.culc = 1
        self.timer = QTimer()
        self.finalstate = 0
        self.time = ''
        for ele in time.localtime()[0:3]:
            self.time += str(ele)
        
        
        settings =QSettings()
        self.re_lastinfo = settings.value("MainWindow/LastDay")
        if self.re_lastinfo != None:
            if str(self.re_lastinfo.split(",")[2]) == '1':
                pass
            elif str(self.re_lastinfo.split(",")[2]) == '2':
                self.label_Info.setText("昨天没有写日记，那么今天呢？")

        self.infomation = "确认离开程序？"
        # self.label_hide.setText("确认离开程序？")
        self.pushButton.clicked.connect(self.startNow)
        self.timer.timeout.connect(self.test)
        # self.finalstate.valuechanged.connect(self.callClose)
        # self.label_hide.textChanged.connect(self.callClose)
    def startNow(self):
        self.hide()
        self.timer.start(2400000)
        self.culc += 1
        self.label_num.setText(str(self.culc) if len(str(self.culc)) > 1 else ' '+str(self.culc))
    
    def test(self):
        # print("ONE LOOP")
        self.show()

    def finishLoop(self):
        self.finalstate = 1
        self.infomation = "咆哮吧，咆哮，怒斥那光的退缩"
        self.close()
        # self.label_hide.setText(self.infomation)

    def unfinishLoop(self):
        self.finalstate = 2
        self.infomation = "好好休息"
        self.close()
        # self.label_hide.setText(self.infomation)

    # def callClose(self):
    #     if self.sender() == QLineEdit:
            
    #         QMessageBox.information(self,"提示",str(self.sender()))
    #     self.close()

    def contextMenuEvent(self,event):
        menu = QMenu()
        finishedAction = menu.addAction("写完了")
        finishedAction.triggered.connect(self.finishLoop)
        if str(self.re_lastinfo.split(",")[2]) != '2':
            unfinishedAction = menu.addAction("今天太累，明天补上")
            unfinishedAction.triggered.connect(self.unfinishLoop)
        settingAction = menu.addAction("配置程序")
        settingAction.triggered.connect(self.showSettingDlg)   
        menu.exec_(event.globalPos())

    def closeEvent(self,event):
        if QMessageBox.information(self,"提示",self.infomation,QMessageBox.Ok|QMessageBox.Cancel) == QMessageBox.Cancel:
            event.ignore()

        settings = QSettings()
        settings.setValue("MainWindow/LastDay",QVariant(self.writeInfo()))
        settings.setValue('Data/'+self.time,QVariant(self.writeInfo()))

    def writeInfo(self):
        info = "%s,%s,%s,%s"%(str(time.ctime()),str(self.culc),str(self.finalstate),str(self.starttime))
        return str(info)

    def showSettingDlg(self):
        settingdlg = appsetting.Form(self)
        if settingdlg.exec_():
            pass

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Daily Notice")
    app.setOrganizationName("Marvin Studio")
    app.setOrganizationDomain("http://www.marvinstudio.cn")
    form = Form()
    from checkandsend import *
    import os,sys,time
    # os.chdir("C:/Users/Administrator/Desktop")
    from tkinter import Tk
    from tkinter.messagebox import showwarning

    try:
        tmp = sys.stdout
        sys.stdout = open('daily.log','a')
        print('\n\n','='*100)
        print('=============================================',time.ctime(),'======================================')
        print('='*100,'\n\n')
        loadfile = open('daily.setting','r')
        thefile = loadfile.read()
        address=str(thefile.split(",")[0])
        dbaddress=str(thefile.split(",")[1])
        # alertaddress = str(thefile.split(",")[4])
        emailaddress=str(thefile.split(",")[2])
        regular=str(thefile.split(",")[3])


        result,infomation,list,notedict= checkDaily(address=address+'/',
                regular=regular,dbaddress=dbaddress)
        if result == True:
            if list != []:
                print('需要写入的数据',list)
                result_2,result_num,result_txt,processinfo,errinfo= sendMail(list,address=address+'/',emailaddress=emailaddress,
                            dbaddress=dbaddress,preparenotedict=notedict)
                print(result_2,'\n',processinfo,'\n',errinfo,'\n',result_txt)
                Tk().withdraw()
                warn_info=showwarning('提示','%s\n%s\n%s'%(processinfo,errinfo,result_txt))
                warn_info
            else:
                print("成功检索数据，但未发现新数据")
                print(infomation,list)
                sys.stdout.close()
                try:
                    form.show()
                    app.exec_()
                except:
                    pass
    except:
        traceback.print_exc()
        print("读取设置出错,请打开程序后右键选择“配置程序”")
        
        settingdlg = appsetting.Form()
        if settingdlg.exec_():
            form.show()
        else:
            form.show()
        app.exec_()

    