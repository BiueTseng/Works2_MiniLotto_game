from PyQt5.QtCore import QThread, pyqtSignal
import random
class MiniLottoThread(QThread):
    phone =pyqtSignal(int)
    def __init__(self,parent = None):
        super().__init__(parent)
        self.runFlag = True
        self.num = random.sample(range(1, 20), 6)
    def run(self):
        self.count = 0
        self.index = 0
        while self.runFlag:
            self.count += 1
            if self.count == 1:
                self.runFlag = False
            while self.index < 6:
                self.index += 1
                print(f'中獎的第{self.index}號碼:{self.num[self.index - 1]}')
                self.phone.emit(self.num[self.index-1])
                self.msleep(1000)



        # for i in range(1,7):
        #     print(i)
        #     self.phone.emit(i)
        #     self.msleep(100)