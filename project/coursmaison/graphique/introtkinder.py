import os, sys
import tkinter
import ImageTk, Image
import time
def test():

    class Application(Frame):
        os.system("say 'click on the button Hello, if you want to see, what happend '")
        def say_hi(self):
            print("hi hello world")
            os.system("say 'hello bod ! '")
        def createWidgets(self):
            self.QUIT = Button(self)
            self.QUIT["text"] = "QUIT"
            self.QUIT["fg"] = "red"
            self.QUIT["command"] = self.quit
            self.QUIT.pack({"side": "left"})

            self.hi_there = Button(self)
            self.hi_there["text"] = "Hello",
            self.hi_there["command"] = self.say_hi

            self.hi_there.pack({"side": "left"})

            

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.pack()
            self.createWidgets()

    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
image = Image.open(image_path+f)
tkpi = ImageTk.PhotoImage(image)        
label_image = tkinter.Label(root, image=tkpi)
label_image.place(x=0,y=0,width=w,height=h)
root.mainloop(0)
