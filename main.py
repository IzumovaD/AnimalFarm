import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import userInterface


def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = userInterface.App()  
    window.show()  
    app.exec_()


if __name__ == '__main__':  
    main() 


