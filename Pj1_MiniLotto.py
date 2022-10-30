import sys
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from Pj1_MiniLottoThread import MiniLottoThread
from ui.ui_project1 import Ui_MainWindow

class MiniLotto(QMainWindow ,Ui_MainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(768,768)
        self.startFlag = False
        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)
        self.btn3.clicked.connect(self.btn3Click)

        self.imgSuccess = QImage("success.jpg")
        self.imgFailed = QImage("failed.jpg")
    def btn1Click(self,event):
        self.msg = self.input1.text()
        # print(self.msg)
        self.lbl6.setText(self.msg)
    def btn2Click(self,event):
        #print("按鈕被按了")
        self.startFlag = not self.startFlag
        if self.startFlag :
            self.btn2.setText("結束抽獎")
            self.l5 = MiniLottoThread()
            self.l5.phone.connect(self.draw)
            self.l5.start()
        else:
            self.btn2.setText("重新開始抽獎")
            self.l5.runFlag = False
        #print(self.l5.num)
    def btn3Click(self,event):
        #print("按鈕被按了")
        #print(self.l5.num)
        #print(self.msg)
        if int(self.msg) in self.l5.num:
            print("中獎")
            self.lblres.setPixmap(QPixmap(self.imgSuccess))
        else:
            print("槓龜")
            self.lblres.setPixmap(QPixmap(self.imgFailed))

    def draw(self,num):
        self.lbl5.setText(f'號碼:{str(num)}')
    def closeEvent(self,event):
        self.l5.runFlag = False
        print("結束程式")


if __name__ =='__main__':
    app = QApplication(sys.argv)
    b = MiniLotto()
    b.show()
    app.exec()