for file_name in os.listdir(this_dir_path):
    if(os.path.isfile(this_dir_path + "\\" + file_name)):
        base_name, extension = os.path.splitext(file_name)
        print("This is file: " + base_name + extension)
    else: 
        print("This is folder: " + file_name)