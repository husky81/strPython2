import os
import numpy as np
import clsSensing
import FileControl
import sys
from PyQt5.QtWidgets import *


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
    mywindow = SimpleQtWindowTest()
    mywindow.show()
    app.exec_()




# configuration
data_folder = os.getcwd() + "/BOTDR실험181010"
data_file_name = "Raw data.txt"

data_file_list = FileControl.find_all_files(data_folder, data_file_name)

ss = []
for fn in data_file_list:
    ss.append(clsSensing.Sensing(fn))

ss[3].show_graph_simple()
