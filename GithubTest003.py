import os
import clsSensing
import FileControl
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupui()

    def setupui(self):
        btn1 = QPushButton("닫기", self)
        btn1.move(20, 20)
        btn1.clicked.connect(app1.quit)


if __name__ == "__main__":
    app1 = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app1.exec_()

form_class = uic.loadUiType("main_window.ui")[0]


class MyMainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_Quit.clicked.connect(self.quit_clicked)

    def quit_clicked(self):
        # self.instance().quit()
        QCoreApplication.instance().quit()
        # app.quit()

    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked")


class SimpleQtWindowTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Review")

        label = QLabel("Hello, PyQt")
        label.move(40, 40)
        # label.show()

        btn1 = QPushButton("Click me", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow2 = MyMainWindow()
    myWindow2.show()
    app.exec_()



# configuration
data_folder = os.getcwd() + "/BOTDR실험181010"
data_file_name = "Raw data.txt"

data_file_list = FileControl.find_all_files(data_folder, data_file_name)

ss = []
for fn in data_file_list:
    ss.append(clsSensing.Sensing(fn))

ss[3].show_graph_simple()
