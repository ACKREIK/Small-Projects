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


# this is a function to get the user input from the text input box
def getInputBoxValue():
    userInput = url.get()
    return userInput


# this is a function to get the selected radio button value
def getRadioButtonValue():
    buttonSelected = fileextension.get()
    return buttonSelected


# this is the function called when the button is clicked
def downloadyt():
    setupdownload()
    # print('clicked')


# this is the function called when the button is clicked
def opengitrepo():
    webbrowser.open(githuburl)
    # os.browse(githuburl)
    # print('clicked')



root = Tk()
#this is the declaration of the variable associated with the radio button group
fileextension = tk.StringVar()



# This is the section of code which creates the main window
root.geometry('774x505')
root.configure(background='#7FFFD4')
root.title('Python Youtube Downloader')


# This is the section of code which creates a text input box
url=Entry(root)
url.place(x=20, y=34)


# This is the section of code which creates a group of radio buttons
frame=Frame(root, width=0, height=0, bg='#76EEC6')
frame.place(x=155, y=34)
ARBEES=[
    ('.MP3', '.mp3'),
    ('.MP4', '.mp4'),
]
for text, mode in ARBEES:
    filetype=Radiobutton(frame, text=text, variable=fileextension, value=mode, bg='#76EEC6', font=('arial', 12, 'normal')).pack(side='top', anchor = 'w')


# This is the section of code which creates the a label
Label(root, text='Python', bg='#7FFFD4', font=('helvetica', 120, 'normal')).place(x=256, y=17)


# This is the section of code which creates the a label
Label(root, text='Youtube', bg='#7FFFD4', font=('helvetica', 100, 'normal')).place(x=264, y=152)


# This is the section of code which creates the a label
Label(root, text='Downloader', bg='#7FFFD4', font=('helvetica', 80, 'normal')).place(x=190, y=250)


# This is the section of code which creates a button
Button(root, text='DOWNLOAD!', bg='#76EEC6', font=('helvetica', 20, 'normal'), command=downloadyt).place(x=15, y=107)


# This is the section of code which creates the a label
Label(root, text='URL', bg='#7FFFD4', font=('helvetica', 20, 'normal')).place(x=25, y=58)


# This is the section of code which creates the a label
Label(root, text='File Type', bg='#7FFFD4', font=('helvetica', 15, 'normal')).place(x=66, y=85)


# This is the section of code which creates the a label
Label(root, text='V 0.8.3', bg='#7FFFD4', font=('helvetica', 15, 'normal')).place(x=701, y=480)


# This is the section of code which creates a button
Button(root, text='Open Github Repo', bg='#76EEC6', font=('helvetica', 15, 'normal'), command=opengitrepo).place(x=7, y=455)


root.mainloop()
