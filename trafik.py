import sys, threading
from PyQt5 import QtWidgets
from mydisain import Ui_MainWindow



class mywindow(QtWidgets.QMainWindow):
    stops = 0
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.exited.clicked.connect(self.exit)
        self.ui.start.clicked.connect(self.__started)
        self.ui.stop.clicked.connect(self.stop)




    def exit(self):
        exit()
    def __started(self):
        mywindow.stops = 0
        self.start()
    def start(self):
        red_1 = threading.Timer(5.0, self.reds)
        self.ui.red.setStyleSheet('QPushButton {background-color: red; color: white;}')
        self.ui.yellow.setStyleSheet('QPushButton {background-color: white; color: white;}')
        self.ui.green.setStyleSheet('QPushButton {background-color: white; color: white;}')
        red_1.start()
        if mywindow.stops == 1:
            red_1.cancel()
    def reds(self):
        yellow_1 = threading.Timer(2.0, self.greens)
        self.ui.yellow.setStyleSheet('QPushButton {background-color: yellow; color: white;}')
        yellow_1.start()
        if mywindow.stops == 1:
            yellow_1.cancel()
    def greens(self):
        green_1 = threading.Timer(5.0, self.yellow_2)
        self.ui.green.setStyleSheet('QPushButton {background-color: green; color: white;}')
        self.ui.red.setStyleSheet('QPushButton {background-color: white; color: white;}')
        self.ui.yellow.setStyleSheet('QPushButton {background-color: white; color: white;}')
        green_1.start()
        if mywindow.stops == 1:
            green_1.cancel()
    def yellow_2(self):
        yellow_2 = threading.Timer(2.0, self.start)
        self.ui.green.setStyleSheet('QPushButton {background-color: white; color: white;}')
        self.ui.yellow.setStyleSheet('QPushButton {background-color: yellow; color: white;}')
        yellow_2.start()
        if mywindow.stops == 1:
            yellow_2.cancel()

    def stop(self):
        mywindow.stops = 1
        yellow_3 = threading.Timer(4.0, self.pause)
        yellow_3.start()
    def pause(self):
        self.ui.red.setStyleSheet('QPushButton {background-color: yellow; color: white;}')
        self.ui.yellow.setStyleSheet('QPushButton {background-color: yellow; color: white;}')
        self.ui.green.setStyleSheet('QPushButton {background-color: yellow; color: white;}')
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())