from tkinter import *
from random import randint


class GUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.button1 = Button(master, text= "Test sensitivity", fg="purple", command=self.test)
        self.button1.pack(side=TOP)
        self.button2 = Button(master, text="Tune sensitivity", fg="pink", command=self.tune)
        self.button2.pack(side=TOP)
        self.button3 = Button(master, text="Setup phone number", fg="green", command=self.setup)
        self.button3.pack(side=TOP)
        self.button4 = Button(master, text="Quit", fg="red", command=self.quit)
        self.button4.pack(side=TOP)

    def test(self):
        print(randint(0, 1))
        #Use this to print current values

    def tune(self):
        pass
        # Use this to tune sensitivity

    def setup(self):
        pass
        # Insert code for phone setup and test


window = Tk()
text = Label(window, text="Lamppost Service Setup")
text.pack()
app = GUI(window)

window.mainloop()
