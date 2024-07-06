import os
import shutil
from notifypy import Notify
import datetime

n = Notify()
cwd = input("Give the Directory: ")
# cwd = os.getcwd()
a = os.listdir(cwd)
print("Files Present: ", a)
num_files = 0
for b in a:
    try:
        index = b.rindex(".")+1
        if(b[index:]=="txt"):
            if (os.path.exists(f"{cwd}\Text")):
                # print("Successfully Shifted!")
                source = f"{cwd}\Text"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "Text")
                os.mkdir(path)
                source = f"{cwd}\Text"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
        elif(b[index:]=="png" or b[index:]=="jpg" or b[index:]=="jpeg"):
            if (os.path.exists(f"{cwd}\Images")):
                source = f"{cwd}\Images"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "Images")
                os.mkdir(path)
                source = f"{cwd}\Images"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

        elif(b[index:]=="pdf"):
            if (os.path.exists(f"{cwd}\PDF")):
                source = f"{cwd}\PDF"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "PDF")
                os.mkdir(path)
                source = f"{cwd}\PDF"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
        elif(b[index:]=="zip"):
            if (os.path.exists(f"{cwd}\ZIP")):
                source = f"{cwd}\ZIP"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "ZIP")
                os.mkdir(path)
                source = f"{cwd}\ZIP"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
       
        elif(b[index:]=="exe"):
            if (os.path.exists(f"{cwd}\EXE")):
                source = f"{cwd}\EXE"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "EXE")
                os.mkdir(path)
                source = f"{cwd}\EXE"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
       
        elif(b[index:]=="csv"or b[index:]=="docx" or b[index:]=="xlsx"):
            if (os.path.exists(f"{cwd}\DOCS")):
                source = f"{cwd}\DOCS"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "DOCS")
                os.mkdir(path)
                source = f"{cwd}\DOCS"
                des = os.path.join(cwd,b)
                num_files += 1
        elif(b[index:]=="msi"or b[index:]=="iso"):
            if (os.path.exists(f"{cwd}\MSI_ISO")):
                source = f"{cwd}\MSI_ISO"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "MSI_ISO")
                os.mkdir(path)
                source = f"{cwd}\MSI_ISO"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
        elif(b[index:]=="ai"):
            if (os.path.exists(f"{cwd}\AI")):
                source = f"{cwd}\AI"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "AI")
                os.mkdir(path)
                source = f"{cwd}\AI"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
        elif(b[index:]=="json"):
            if (os.path.exists(f"{cwd}\JSON")):
                source = f"{cwd}\JSON"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "JSON")
                os.mkdir(path)
                source = f"{cwd}\JSON"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
        elif(b[index:]=="json"):
            if (os.path.exists(f"{cwd}\JSON")):
                source = f"{cwd}\JSON"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "JSON")
                os.mkdir(path)
                source = f"{cwd}\JSON"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
        elif(b[index:]=="mp3" or b[index:]=="m4a" or b[index:]=="wav"):
            if (os.path.exists(f"{cwd}\Audio")):
                source = f"{cwd}\Audio"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "Audio")
                os.mkdir(path)
                source = f"{cwd}\Audio"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
        elif(b[index:]=="mp4" or b[index:]=="mov"):
            if (os.path.exists(f"{cwd}\Vidoes")):
                source = f"{cwd}\Videos"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1

            else:
                print("Making the directory And Shifting the file")
                path = os.path.join(cwd, "Videos")
                os.mkdir(path)
                source = f"{cwd}\Videos"
                des = os.path.join(cwd,b)
                shutil.move(des,source)
                num_files += 1
    except:
        print(f"{b} is a Folder")

if num_files > 0:
    n.title = "File Manager"
    n.message = "Successfully Shifted files : " + str(num_files)
    n.icon = "E:\CodesGround\python\Logs\icon-removebg-preview.png"
    n.send()
    logs = f"{os.getcwd()}\\Logs\\filemanagerLog.txt"
    f = open(logs, "a")
    f.write(f"{datetime.datetime.now()} Script Ran! \n")
else:
    n.title = "File Manager"
    n.message = "Files not availble!"
    logs = f"{os.getcwd()}\Logs\icon-removebg-preview.png"
    n.icon = logs
    n.send()