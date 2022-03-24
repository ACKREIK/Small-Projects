# deps
import os
import shutil
# variables

# gaming script
directory = "C:\\"
print("Type /help for help")
print("Items in directory " + directory + " :")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)  # pro
while True:
    print("Directory:", directory)
    cmd = input("Enter Command: ")
    if cmd == "/scan":
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print(f)
    if "/cd" in cmd:
        directory = cmd.replace("/cd ", "", 1)
        # directory
    if cmd == "/cmd":
        os.system("start cmd")
    if cmd == "/exit":
        exit(0)
        break
    if "/runcmd" in cmd:
        os.system("start cmd /c "+cmd.replace("/runcmd ", "", 1))
    if cmd == "/move":
        root = input("File Location (Ex: C:\\Users\\Human\\ez.zip): ")
        location = input("Output File Location (Ex: C:\\Users\\Human\\Downloads): ")
        shutil.move(root, location)
    if cmd == "/help":
        print("Commands:")
        print("/cd Directory - Go to specified Directory")
        print("/scan - print out directory")
        print("/help - gives help")
        print("/cmd - opens command prompt")
        print("/exit - close file browser")
        print("/move - moves a file")
