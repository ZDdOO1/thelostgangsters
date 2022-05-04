from tkinter import *
from random import randint
from twilio.rest import Client
from PiAnalog import *
from guizero import App, Text
import time, math

class GUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.button1 = Button(master, text="Test LED", bg="cyan", command=self.test)
        self.button1.pack(side=TOP, fill=X)
        self.button2 = Button(master, text="Setup phone number", bg="green", command=self.setup)
        self.button2.pack(side=TOP, fill=X)
        self.button3 = Button(master, text="Quit", bg="red", command=self.stop)
        self.button3.pack(side=TOP, fill=X)
        
    def test(self):
        #starts reading light levels
        startReading()
        
    def stop(self):
        #program
        exit()
        
    def setup(self):
        num = Label(window, text="Phone Number", bg="green")
        num.pack(side=TOP, fill=X)
        value = Label(window, text="3185138033", bg="green")
        value.pack(side=TOP, fill=X)


class TextMessage():

    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        self._phoneNumber = value

    def sendText(self, phoneNumber):
        #Never leave sid and token in code when pushing to github
        account_sid = "AC3011ed2449a037259ba00c392b44cc82"
        auth_token = "11a285608af1e1a14b8c928c4a3bf5ad"
        client = Client(account_sid, auth_token)
        message = client.api.account.messages.create(
            to=phoneNumber,
            from_="+18507862013", #Twilio default number
            body="The lights are out!")
    '''
    def setUpNumber(self,pNum):
        client = Client(account_sid, auth_token)
        validation_request = client.validation_requests \
                           .create(
                                friendly_name='Test Number',
                                phone_number=pNum)
        print(validation_request.friendly_name)
        '''
    
p = PiAnalog()

def light_from_r(R):
    #Use this for text message
    return math.log(1000000.0/R) * 10.0
    
def update_reading():
        light = light_from_r(p.read_resistance())
        reading_str = "{:.0f}".format(light)
        if(int(reading_str) <= 15):
            t1 = TextMessage("+3185138033")
            t1.sendText("+13185138033")
            light_text.size = 12
            light_text.value = "Text Message Sent! \nLight Value was: {}".format(reading_str)
            return
        light_text.value = reading_str
        light_text.after(200, update_reading)
        
def startReading():
    light_text.size = 110
    light_text.after(200, update_reading)
    #app.display()
    
#gui for light level
app = App(title= "Light Meter", width= "400", height= "300")
Text(app, text= "Light", size=32)
light_text = Text(app, text="0", size=110)

#gui for settings
window = Tk()
text = Label(window, text="Lamppost Service Setup")
text.pack()
app = GUI(window)
window.mainloop()
