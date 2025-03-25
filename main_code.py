# news gui
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
import webbrowser

class NewsApp:

    def __init__(self):
        
        #fetching news from newsapi
        self.data = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=b089d64b678a412f92460cb20cca161b').json()

        #creating a GUI window
        self.load_gui()
        

        #load the first news item
        self.load_news_item(0)
  

    def load_gui(self):
        self.root = Tk()
        self.root.title('News App')
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.configure(bg='white')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):
        #clear the screen for the new item
        self.clear()

        #image
        try:
            image_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(image_url).read()  #downloading the image and storing it in raw_data and it is in bytes
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))  #converting the bytes to image and saving it in the current directory
            photo = ImageTk.PhotoImage(im)

        except:
            image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7fB9QYpMpkv92isdgg9sMPlFSZvFiV8_1tPo_1gRrMqu-e94YzqijCNM&s'
            raw_data = urlopen(image_url).read()  #downloading the image and storing it in raw_data and it is in bytes
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))  #converting the bytes to image and saving it in the current directory
            photo = ImageTk.PhotoImage(im)
               

        label = Label(self.root,image = photo)
        label.pack()

        heading = Label(self.root,text = self.data['articles'][index]['title'],font=('Arial',14,'bold'),bg='white',fg='black', wraplength=350, justify = 'center')
        heading.pack(pady=(10,20))

        details = Label(self.root,text = self.data['articles'][index]['description'],font=('Arial',12),bg='white',fg='black', wraplength=350, justify = 'center')
        details.pack(pady=(2,20))

        frame = Frame(self.root,bg='white')
        frame.pack(expand = True, fill = 'both')

        if index != 0:

            prev = Button(frame,text = '<<prev',width = 16, height=3, command= lambda: self.load_news_item(index-1))
            prev.pack(side='left')

        read = Button(frame,text = 'Read More',width = 16, height=3, command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side='left')

        if index != len(self.data['articles'])-1:

            next = Button(frame,text = 'next>>',width = 16, height=3, command= lambda: self.load_news_item(index+1))
            next.pack(side='left')   

        


        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()



