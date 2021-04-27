from PyQt5 import uic, QtWidgets
# from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication, QPushButton

Form, Window = uic.loadUiType("trancifik.ui")


class Ui(QtWidgets.QDialog, Form):
    color = 'red'
    def __init__(self):
        super().__init__()
        self.click = QPushButton("exited", self)

        self.click.clicked.connect(self.clic)
    def clic(self):
        print('click')



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    tst = Ui()
    tst.show()
    sys.exit(app.exec_())

