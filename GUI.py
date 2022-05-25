from tkinter import *
from PIL import Image, ImageTk
from assistant import assistant,Listen_name

class AnimateGifLabel(Label):
    def __init__(self, *argv, image = None,  **kwargs):
        self.master = 0
        self.filename = image
        self.check_cadrs()
        self.i = 0
        self.img = Image.open(image)
        self.img.seek(0)
        self.image = ImageTk.PhotoImage(self.img)
        super().__init__(*argv, image = self.image, **kwargs)
        if 'delay' in kwargs:
            self.delay = kwargs['delay']
        else:
            try:
                self.delay = self.img.info['duration']
            except:
                self.delay = 100
        self.after(self.delay, self.show_new_cadr)


    def check_cadrs(self):
        self.cadrs = Image.open(self.filename).n_frames
    def show_new_cadr(self):
        if self.i == self.cadrs:
            self.i=0
        self.img.seek(self.i)
        self.image = ImageTk.PhotoImage(self.img)
        self.config(image = self.image)
        self.i+=1
        self.master.after(self.delay, self.show_new_cadr)
root=Tk()
root.title("IONIC VOICE ASSISTANT")
canvas=Canvas(root,width=800,height=600)

image=AnimateGifLabel(image = '123.gif')

canvas.create_window(0,0,anchor=NW,window=image)
canvas.pack()

button = Button(root, text="Speak To Me ")
dwnd = PhotoImage(file='voice-visualization.gif')
button.config(command=Listen_name,image=dwnd,height=200,width=800,borderwidth = 0)
button.pack() # Displaying the button
root.mainloop()
