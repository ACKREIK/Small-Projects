# deps
import shutil
# vars
root = "A"
location = "A"
while True:
    root = input("File Location (Ex: C:\\Users\\Human\\ez.zip): ")
    location = input("Output File Location (Ex: C:\\Users\\Human\\Downloads): ")
    shutil.move(root, location)
    choice = input("Move Another File? Y/N: ")
    if choice == "Y" or choice == "y":
        print("Looping")
    else:
        print("Exiting")
        exit()
        break
