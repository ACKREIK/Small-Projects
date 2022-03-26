import os
# import pytube
from pytube import YouTube
import tkinter as tk
import webbrowser
# from tkinter import ttk
from tkinter import *
# from tkinter import filedialog
from tkinter import messagebox
wd = os.getcwd()
githuburl = "https://ackreik.github.io/Small-Projects/"


# download an video from youtube via, args are (url, name)
def download(url, name):
    yt = YouTube(url)
    yt.streams.first().download(wd, filename=name)
    messagebox.showinfo("Download", "Downloaded File!")


def setupdownload():
    url = getInputBoxValue()
    extension = getRadioButtonValue()
    print(extension, url)
    # name = "INPUT"
    if extension == '.mp4':
        name = "DownloadedVideo.mp4"
        download(url, name)
    elif extension == '.mp3':
        name = "DownloadedAudio.mp3"
        download(url, name)


# GUI


# this is a function to get the selected radio button value
def getRadioButtonValue():
    buttonSelected = fileextension.get()
    return buttonSelected


# this is a function to get the user input from the text input box
def getInputBoxValue():
    userInput = url.get()
    return userInput


# this is the function called when the button is clicked
def btnClickFunction():
    setupdownload()


# this is the function called when the button is clicked
def opengitrepo():
    webbrowser.open(githuburl)



root = Tk()
#this is the declaration of the variable associated with the radio button group
fileextension = tk.StringVar()



# This is the section of code which creates the main window
root.geometry('870x580')
root.configure(background='#F0F8FF')
root.title('Python Youtube Downloader 2')


# This is the section of code which creates a group of radio buttons
frame=Frame(root, width=0, height=0, bg='#E0EEEE')
frame.place(x=585, y=32)
ARBEES=[
    ('.MP4 File', '.mp4'),
    ('.MP3 File', '.mp3'),
]
for text, mode in ARBEES:
    fileextensionselecter=Radiobutton(frame, text=text, variable=fileextension, value=mode, bg='#E0EEEE', font=('arial', 24, 'normal')).pack(side='top', anchor = 'w')


# This is the section of code which creates a text input box
url=Entry(root)
url.place(x=445, y=82)


# This is the section of code which creates the a label
Label(root, text='Python', bg='#F0F8FF', font=('arial', 50, 'normal')).place(x=15, y=12)


# This is the section of code which creates the a label
Label(root, text='Youtube', bg='#F0F8FF', font=('arial', 50, 'normal')).place(x=15, y=112)


# This is the section of code which creates the a label
Label(root, text='Downloader', bg='#F0F8FF', font=('arial', 80, 'normal')).place(x=5, y=212)


# This is the section of code which creates the a label
Label(root, text='Instructions: Put in url, select format, hit download.', bg='#F0F8FF', font=('arial', 20, 'normal')).place(x=5, y=542)


# This is the section of code which creates the a label
Label(root, text='0.9.1', bg='#F0F8FF', font=('arial', 20, 'normal')).place(x=805, y=552)


# This is the section of code which creates the a label
# This is the section of code which creates the a label
Label(root, text='Link:', bg='#F0F8FF', font=('arial', 20, 'normal')).place(x=445, y=42)


# This is the section of code which creates the a label
Label(root, text='Format', bg='#F0F8FF', font=('arial', 30, 'normal')).place(x=585, y=162)


# This is the section of code which creates a button
Button(root, text='Download!', bg='#C1CDCD', font=('arial', 20, 'normal'), command=btnClickFunction).place(x=405, y=142)


# This is the section of code which creates a button
Button(root, text='Open GitHub', bg='#838B8B', font=('arial', 20, 'normal'), command=opengitrepo).place(x=5, y=482)


root.mainloop()
