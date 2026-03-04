# -*- coding: utf-8 -*-
# @Time    : 2026/1/31 下午10:48
# @Author  : hjx
# @File    : 01窗口.py

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口大小
        self.resize(400, 300)
        # 设置窗口位置
        self.move(600, 300)
        # 设置标题
        self.setWindowTitle('这是一个pyqt窗体')

        # 创建标签
        self.label = QLabel(self)
        self.label.setText('这是标签')
        self.label.move(100, 200)

        # 创建按钮
        self.button = QPushButton(self)
        self.button.setText('按钮')
        self.button.move(200, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # sys.argv 能从命令行接受一些参数
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())   # 让其运行起来