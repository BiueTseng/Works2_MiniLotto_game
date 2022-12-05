from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from Pj1_MiniLottoThread import MiniLottoThread
from ui.ui_project1_v2 import Ui_MainWindow
import sys ,sqlite3 , random
import matplotlib.pyplot as plt
import numpy as np
# from PIL import Image, ImageSequence
# import cv2
class MiniLotto(QMainWindow ,Ui_MainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        # self.resize(768,768)
        self.startFlag = False
        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)
        self.btn3.clicked.connect(self.btn3Click)
        self.btn4.clicked.connect(self.btn4Click)
        #設定圖片
        self.imgSuccess = QImage("success.jpg")
        self.imgFailed = QImage("failed.jpg")
    def btn1Click(self):
        self.msg = self.input1.text()
        print(type(self.msg))
        self.res2.setText(self.msg)
    def btn2Click(self):
        #print("按鈕被按了")
        self.auto_num = random.randint(1,20)
        self.res2.setText(str(self.auto_num))

    def btn3Click(self):
        #print("按鈕被按了")
        # self.img = Image.open('waiting.gif')
        # self.loop = True
        # while self.loop:
        #     for frame in ImageSequence.Iterator(self.img):
        #         frame = frame.convert('RGB')
        #         self.cv2_frame = np.array(frame)
        #         self.show_frame = cv2.cvtColor(self.cv2_frame, cv2.COLOR_RGB2BGR)
        #         cv2.imshow('wait.gif', self.show_frame)
        #         if cv2.waitKey(40) == ord('q'):
        #             self.loop = False
        #             break
        self.startFlag = not self.startFlag
        if self.startFlag :
            self.btn3.setText("開 獎")
            self.r1 = MiniLottoThread()
            self.r1.phone.connect(self.minilottoThreadphone)
            self.r1.phone2.connect(self.minilottoThreadphone2)
            self.r1.start()

    def btn4Click(self):
        # print("分析按鈕被按了")
        #建立資料庫連線
        conn = sqlite3.connect('analyze.db')
        #建立鼠標
        cursor = conn.cursor()
        # 讀取資料庫
        cmd = '''SELECT N1,N2,N3,N4,N5,N6 from Numdb'''
        cursor.execute(cmd)
        data = []
        count = int()
        for d in cursor.fetchall():
            count += 1
            for i in d:
                data.append(i)
        #Data Cleansing
        freq_data = []
        for i in sorted(set(data)):
            freq_data.append(data.count(i)/len(data))

        #關閉資料庫連線
        conn.commit()
        conn.close()
        self.analysisPlot(data,freq_data,count)

    def minilottoThreadphone(self, num):
        self.text = self.res1.setText(num)
        self.disabledGui()
    def minilottoThreadphone2(self,result):
        self.result = result
        if result ==True:
            self.enabledGui()
            if int(self.msg) in self.r1.num:
                print("中獎")
                self.pic_res.setPixmap(QPixmap(self.imgSuccess))
            else:
                print("槓龜")
                self.pic_res.setPixmap(QPixmap(self.imgFailed))
            self.startFlag = False
            self.btn3.setText("開始抽獎")
    def analysisPlot(self,real_data,sorted_data,count):
        plt.figure(figsize=(4.5, 5.8))
        plt.barh(range(1, 21), sorted_data, tick_label=range(1, 21), color='#3e82fc')
        plt.xticks(np.arange(0, 0.1, 0.01))
        plt.axvline(x=0.05 - 2 * pow((0.05 * 0.95 / len(real_data)), 0.5), c='#c74767', ls='--')
        plt.axvline(x=0.05 + 2 * pow((0.05 * 0.95 / len(real_data)), 0.5), c='#c74767', ls='--')
        plt.title(f'Cumulative distribution of the {count}th number')
        plt.xlabel("Probability")
        plt.ylabel("Number")
        # plt.show()
        plt.savefig('analysis.png')
        self.imgAnalysis = QImage("analysis.png")
        self.imgAnalysis = self.imgAnalysis.scaled(480, 495)
        self.ana_res.setPixmap(QPixmap(self.imgAnalysis))
    def disabledGui(self):
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)

    def enabledGui(self):
        self.btn1.setEnabled(True)
        self.btn2.setEnabled(True)
        self.btn3.setEnabled(True)

    def closeEvent(self,event):
        self.r1 = False
        print("結束程式")


if __name__ =='__main__':
    app = QApplication(sys.argv)
    b = MiniLotto()
    b.show()
    app.exec()