# install pytube3
#pip install pytube3

from tkinter import filedialog
from tkinter import *
from pytube import YouTube

root = Tk()

download_path = StringVar(root)
youtube_link = StringVar(root)

def getpath():
    path = filedialog.askdirectory();
    download_path.set(path)
    
def download():
    Youtube_link = youtube_link.get() 
    Folder = download_path.get() 
    getVideo = YouTube(Youtube_link) 
    videoStream = getVideo.streams.first() 
    videoStream.download(Folder)
    
    root1 = Tk()
    root1.title('Message Box')
    root1.geometry('100x100')
    l3 = Label(root1,text = 'DownloadSuccessfully').pack()
    
    
    

root.geometry('600x150');
root.title('Youtube Downloader')
url_entry = Label(root,text = 'Enter the Url').pack()
get_url = Entry(root,width = 200,textvariable = youtube_link).pack()
path_entry = Label(root,text = 'Enter the Path').pack()
get_path = Entry(root,width = 200,textvariable = download_path).pack()
btn1 = Button(root,text = 'Browse',command = getpath).pack()
btn2 = Button(root,text = 'Download', command = download).pack()


root.mainloop()
