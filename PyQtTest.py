#!/user/bin/python2
# -*- coding:utf-8 -*-
'''''
Creat a simple window
'''
__author__ = 'CHN Long'

import sys
from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    w.setWindowTitle("Hello PyQt5")
    sys.exit(app.exec_())