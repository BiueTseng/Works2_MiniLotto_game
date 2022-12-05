from PyQt5.QtCore import QThread, pyqtSignal
import random
import sqlite3
class MiniLottoThread(QThread):
    phone = pyqtSignal(object)
    phone2 = pyqtSignal(object)
    def __init__(self):
        super().__init__(None)
        self.runFlag = True
        self.num = random.sample(range(1, 21), 6)
        self.result = False
        conn = sqlite3.connect("analyze.db")
        cursor = conn.cursor()
        cursor.execute('''create table if not exists Numdb (ID integer primary key autoincrement,
                                N1 int,N2 int,N3 int,N4 int,N5 int,N6 int);
                            ''')
        cursor.execute("insert into Numdb (N1, N2, N3, N4, N5, N6) values (?, ?, ?, ?, ?, ?)", self.num)
        conn.commit()
        conn.close()
    def run(self):
        lock = 0
        index = 0
        while self.runFlag:
            self.text =''
            lock += 1
            if lock == 1:
                self.runFlag = False
            while index < 6:
                index += 1
                print(f'中獎的第{index}號碼:{self.num[index - 1]}')
                self.msg = self.num[index-1]

                if index ==6:
                    self.text += f'{str(self.msg)}'
                else:
                    self.text += f' {str(self.msg)} .'
                self.phone.emit(self.text)
                self.msleep(600)
                if index ==6:
                    self.result = True
                    self.phone2.emit(self.result)



        # for i in range(1,7):
        #     print(i)
        #     self.phone.emit(i)
        #     self.msleep(100)