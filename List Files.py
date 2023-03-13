import os
import shutil

source = "C:/Users/karan/Desktop"
destination = "C:/Users/karan/Desktop/FILES"
list_of_files = os.listdir(source)
print(list_of_files)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    print(name)
    print(ext)
    if (ext == ""):
        continue
    if (ext in ['.pdf','.pptx','.doc','.docx','.txt']):
        path1 = source+"/"+file_name
        path2 = destination+"/"+file_name
        if os.path.exists(destination):
            print("MOVING....."+file_name)
            shutil.move(path1,path2)
        else:
            os.makedir(destination)
            print("MOVING....."+file_name)
            shutil.move(path1,path2)
            