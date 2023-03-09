import os
import shutil

from_dir = "C:\\Users\\Kalpa Kularathne\\Downloads"
to_dir = "C:\\Users\\Kalpa Kularathne\\Documents\\Python Class\\Projects\\Project 102"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    file_name, ext = os.path.splitext(file)

    if ext == "":
        continue

    elif ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + '\\' + file
        path2 = to_dir + '\\' + "Document_Files"
        path3 = to_dir + '\\' + "Document_Files" + '\\' + file_name + ext

        if os.path.exists(path2):
            print("Moving " + file_name + ".....")

            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")

            shutil.move(path1, path3)
