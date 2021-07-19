# https://www.tutorialspoint.com/python/os_file_methods.htm
import os   

# https://www.tutorialspoint.com/high-level-file-operations-in-python-shutil
import shutil


if (os.path.exists("demofile.txt")):
    os.remove("demofile.txt")

if (os.path.exists("demofil3.txt")):
    os.remove("demofile.txt")

# ------------------------------------------------------------------------------------

f = open("demofile.txt", "a")
f.write("demofile")
f.close()

# append content to file
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# over write the file
f = open("demofile2.txt", "w")
f.write("Now the file has more content!")
f.close()

#open and read the file:
f = open("demofile2.txt", "r")
print(f.read())
f.close()

# ------------------------------------------------------------------------------------

# copy a single file
shutil.copy("demofile2.txt", "demofile3.txt")

# ------------------------------------------------------------------------------------

if (os.path.exists("test-folder")):
    os.rmdir("test-folder")
    
if (os.path.exists("test-folder2")):
    os.rmdir("test-folder2")

os.mkdir("test-folder")

# ------------------------------------------------------------------------------------

if (os.path.exists("test-folder")):
    shutil.copytree("test-folder", "test-folder2")

# ------------------------------------------------------------------------------------

this_file_name = __file__
print(this_file_name)
this_dir_path = os.path.dirname(this_file_name)
print(this_dir_path)

# ------------------------------------------------------------------------------------

for file_name in os.listdir(this_dir_path):
    if(os.path.isfile(this_dir_path + "\\" + file_name)):
        base_name, extension = os.path.splitext(file_name)
        print("This is file: " + base_name + extension)
    else: 
        print("This is folder: " + file_name)




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
    button.click()

    win.show()
    sys.exit(app.exec_())

  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 