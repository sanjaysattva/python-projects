import tkinter
from tkinter import * 
from Pytube import YouTube 

root = Tk()
root.title("youtube video downloader")
root.geometry('700x700')
link = StringVar() #variable type
def download():
    url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
    video = url.streams.first() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
    video.download() # This is the method with the instruction to download the video.
    Label(root, text="Downloaded", font="arial 15").place(x=100, y=120)


entrybtn=Entry(root,textvariable=link,
width=25,font = ('arial', 20, 'bold')).grid(row=2,column=3)

submitbtn = Button(root,text = "enter",command= download,bg="DodgerBlue2",
fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3)

mainloop()
