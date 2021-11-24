import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle('Кофе')
        self.con = sqlite3.connect("coffee_db.sqlite")
        self.cur = self.con.cursor()
        self.dobav_tabl()

    def dobav_tabl(self):
        zapr_tb = self.cur.execute("""SELECT * FROM info_coffee""").fetchall()
        print(zapr_tb)
        self.rowPosition = self.table.rowCount()
        for i in range(len(zapr_tb)):
            self.table.insertRow(self.rowPosition)
            for j in range(7):
                if j != 2 and j != 3:
                    self.table.setItem(self.rowPosition, j, QTableWidgetItem(str(zapr_tb[i][j])))
                elif j == 2:
                    f = self.cur.execute(f"""SELECT title FROM degree_of_roast 
                    WHERE id = {zapr_tb[i][j]}""").fetchall()
                    self.table.setItem(self.rowPosition, j, QTableWidgetItem(str(f[0][0])))
                elif j == 3:
                    k = 'Молотый' if str(zapr_tb[i][j]) == '1' else 'В зернах'
                    self.table.setItem(self.rowPosition, j, QTableWidgetItem(k))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
