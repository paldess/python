from PyQt5 import QtWidgets
from mydisain import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.exited.clicked.connect(self.btnClicked)

    def btnClicked(self):
        self.ui.red.addItem('sdfsdfsd')

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())