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