import kivy
from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from functools import partial
import time
import requests

class SwitchContainer(GridLayout): #Create a class that uses the GridLayout module
    def __init__(self, **kwargs):
          
        super(SwitchContainer, self).__init__(**kwargs)
        self.cols = 2

        #
        #Switch1
        #
          
        #switch label
        self.add_widget(Label(text="SW 1: "))

        #switch1 button
        self.sw1 = Switch(active=False)
        self.add_widget(self.sw1)
        self.sw1.disabled = True  #Make the switch unclickable on the app 


        #
        #Led1
        #
        
        #led label
        self.add_widget(Label(text="LED 1: ")) #Create a label that displays "LED 1"
    
        #led1 button
        self.led1 = Switch(active=False)
        self.add_widget(self.led1) #Create a switch that can be turned off or on

        #schedule the JSONrequest function to trigger every second to read/write database
        event = Clock.schedule_interval(partial(self.JSONrequest), 1)

    #Make sure this following function’s indentation matches with the def __init__ function above
    def JSONrequest(self, *largs):
        #Get the sw1 active status and convert it to an integer
        if (self.sw1.active == True):
            SW1 = 1    
        else:
            SW1 = 0

        #Get the led1 active status and convert it to an integer
        if (self.led1.active == True):
            LED1 = 1              
        else:
            LED1 = 0
         
          
          
        #json request
        data = {'username': 'ben','password':'benpass', 'SW1':SW1, 'LED1': LED1}
        res = requests.post("https://yourdomain.000webhostapp.com/scripts/sync_app_data.php", json=data)
        r = res.json()


        #If the app sw1 doesn't match the DB sw1, change it on the app.
        if SW1 != r['SW1']:
            print("Changing SW1 status to the value in the database.")
            if self.sw1.active == True:
                self.sw1.active = False
            else:
                self.sw1.active = True
        else:
            return

class SwitchExample(App):
    def build(self):
        return SwitchContainer()


if __name__ == '__main__':
     SwitchExample().run()
