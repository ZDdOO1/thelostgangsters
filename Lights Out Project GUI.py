from tkinter import *
from random import randint
#from twilio.rest import Client

class GUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.button1 = Button(master, text= "Test sensitivity", bg="purple", command=self.test)
        self.button1.pack(side=TOP, fill=X)
        self.button2 = Button(master, text="Tune sensitivity", bg="pink", command=self.tune)
        self.button2.pack(side=TOP, fill=X)
        self.button3 = Button(master, text="Setup phone number", bg="green", command=self.setup)
        self.button3.pack(side=TOP, fill=X)
        self.button4 = Button(master, text="Quit", bg="red", command=self.quit)
        self.button4.pack(side=TOP, fill=X)

    def test(self):
        print(randint(0, 1))
        #Use this to print current values

    def tune(self):
        pass
        # Use this to tune sensitivity

    def setup(self):
        num = Label(window, text="Phone Number", bg="green")
        num.pack(side=TOP, fill=X)

        value = Entry(window, bg="green")
        value.pack(side=TOP, fill=X)



class TextMessage():
    #Default sid and auth token from twilio
    account_sid = ""
    auth_token = ""

    def __init__(self,phoneNumber):
        this.phoneNumber = phoneNumber

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        self._phoneNumber = value

    def sendText(self, phoneNumber):
        client = Client(account_sid, auth_token)
        message = client.api.account.messages.create(
            to=phoneNumber,
            from_="+1850762013",
            body="sussy baka")


window = Tk()
text = Label(window, text="Lamppost Service Setup")
text.pack()
app = GUI(window)

window.mainloop()
