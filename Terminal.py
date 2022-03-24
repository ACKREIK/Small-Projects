# deps
import os
import shutil
# variables
#
# gaming script
global directory
directory = "C:\\"

if directory:
    print("yes")
print("Type /help for help")
print("Items in directory " + directory + " :")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)  # pro


def newdirec(path):
    global directory
    directory = path


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
    if cmd == "/ping":
        import requests

        print("Ping")
        site = input("Enter Site URL:")
        data = requests.get(site)
        if data:
            print("Pong!")
        else:
            print("Fuck.")
    if cmd == "/gui":

        from tkinter import *

        # this is the function called when the button is clicked
        def setdirectory():
            newdirec(Path.get())
            # print('clicked')


        # this is a function to get the user input from the text input box
        def getInputBoxValuepath():
            userInput = Path.get()
            return userInput


        # this is the function called when the button is clicked
        def scandirectory():
            print("Scanning current directory, : ", directory)
            # print('clicked')
            for nam in os.listdir(directory):
                ro = os.path.join(directory, nam)
                # checking if it is a file
                if os.path.isfile(ro):
                    print(ro)

        # this is the function called when the button is clicked
        def opencmd():
            os.system("start cmd")
            # print('clicked')


        # this is the function called when the button is clicked
        def exitterminal():
            exit(0)
            # print('clicked')


        # this is the function called when the button is clicked
        def movefile():
            output = getInputBoxValueoutput()
            input = getInputBoxValueoriginal()
            shutil.move(input, output)

            # print('clicked')


        # this is a function to get the user input from the text input box
        def getInputBoxValueoriginal():
            userInput = originalpath.get()
            return userInput


        # this is a function to get the user input from the text input box
        def getInputBoxValueoutput():
            userInput = outputpath.get()
            return userInput


        # this is the function called when the button is clicked
        def help():
            import webbrowser
            webbrowser.open("https://github.com/ACKREIK/Small-Projects", new=0, autoraise=True)
            # print('clicked')



        root = Tk()

        # This is the section of code which creates the main window
        root.geometry('444x293')
        root.configure(background='#7FFFD4')
        root.title('Terminal Gui')


        # This is the section of code which creates a button
        Button(root, text='Set Directory', bg='#66CDAA', font=('arial', 12, 'normal'), command=setdirectory).place(x=11, y=52)


        # This is the section of code which creates a text input box
        Path=Entry(root)
        Path.place(x=129, y=52)


        # This is the section of code which creates a button
        Button(root, text='Scan Current Directory', bg='#66CDAA', font=('arial', 12, 'normal'), command=scandirectory).place(x=12, y=15)


        # This is the section of code which creates the a label
        Label(root, text='Directory Input', bg='#7FFFD4', font=('arial', 12, 'normal')).place(x=133, y=68)


        # This is the section of code which creates a button
        Button(root, text='Open Command Prompt', bg='#66CDAA', font=('arial', 12, 'normal'), command=opencmd).place(x=12, y=88)


        # This is the section of code which creates a button
        Button(root, text='Exit', bg='#FF4040', font=('arial', 12, 'normal'), command=exitterminal).place(x=386, y=254)


        # This is the section of code which creates a button
        Button(root, text='Move File', bg='#458B74', font=('arial', 12, 'normal'), command=movefile).place(x=12, y=126)


        # This is the section of code which creates a text input box
        originalpath=Entry(root)
        originalpath.place(x=110, y=127)


        # This is the section of code which creates a text input box
        outputpath=Entry(root)
        outputpath.place(x=249, y=128)


        # This is the section of code which creates the a label
        Label(root, text='Input File Path', bg='#7FFFD4', font=('arial', 12, 'normal')).place(x=122, y=146)


        # This is the section of code which creates the a label
        Label(root, text='Output Path', bg='#7FFFD4', font=('arial', 12, 'normal')).place(x=262, y=147)


        # This is the section of code which creates a button
        Button(root, text='HELP', bg='#66CDAA', font=('arial', 12, 'normal'), command=help).place(x=13, y=168)


        root.mainloop()

    if cmd == "/help":
        print("Commands:")
        print("/cd Directory - Go to specified Directory")
        print("/scan - print out directory")
        print("/help - gives help")
        print("/cmd - opens command prompt")
        print("/exit - close file browser")
        print("/move - moves a file")
        print("/gui - use the BETA gui")
