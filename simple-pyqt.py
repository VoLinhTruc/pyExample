
import sys

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500,350,300,100) 
    win.setWindowTitle("test") 

    button = QPushButton("OK", win)
    button.setGeometry(0, 0, 50, 30)
    button_width = int(win.width()/2 - button.width()/2)
    button_height = int(win.height()/2 - button.height()/2)
    button.setGeometry(button_width,  button_height, 50, 30)
    button.clicked.connect(lambda: exit())
    # button.click()

    win.show()
    sys.exit(app.exec_())

  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 