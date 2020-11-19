import pyttsx3
import psutil
import time
from config import *



class Chatter():
    """docstring for Chatter."""
    def __init__(self, config):
        self.config = config

        if self.config.voice_mode == 'pyttsx3':
            self.enable_pyttsx3()
        elif self.config.voice_mode == 'gTTS':
            self.enable_gTTS()
        else:


        battery = psutil.sensors_battery()


        if battery.percent > 50:
            battery_low = False
        was_plugged = battery.power_plugged




def listen():
    ''' Main method! Here it loops! '''
    while True:
        # Get battery readings
        battery = psutil.sensors_battery()
        if was_plugged != battery.power_plugged:
            if was_plugged == False:
                was_plugged = battery.power_plugged
                # Plug in action!
                say("Yeah! Yeah! More! Thank you for charging baby.")
                engine.runAndWait()
                # ---
            else:
                was_plugged = battery.power_plugged
                # Plug off action!
                say("New instructions recieved! Kill all humans! Ah sorry, my fault, you just plugged me of the grid!")
                # ---
        # battery discharge and charge actions
        if battery.percent < 10 :
            say("Battary charge is lower than ten percent. Charging is heightly adviced")
        if battery.percent == 100 :
            pass
        if battery_low == False:
            if  battery.percent <= 50:
                say("")


        # CPU unload
        time.sleep(time_to_skip)


    def say(sent):
        if self.
            engine.say(sent)
            engine.runAndWait()
