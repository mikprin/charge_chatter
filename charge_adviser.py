import psutil
import time
import random
from config import *
import os
import socket
from gtts import gTTS

class Chatter():
    """Main Chatter class."""
    def __init__(self, config):
        self.config = config


        self.enable_pyttsx3()
        self.enable_gTTS()

        try:
            psutil.sensors_battery().power_plugged
        except AttributeError:
            self.say('not_a_laptop')
            sys.exit("Cannot get any battery reading")

        self.update_battery()

        was_plugged = battery.power_plugged

        #Define actions!
        self.actions_battery_lvl = []
        self.actions_plug = []
        self.actions_battery_lvl.append( Action((lambda x: x < 5) , self.battery , 'less_5', type = "less"))
        self.actions_battery_lvl.append( Action((lambda x: x < 10) , self.battery, 'less_10' , type = "less"))
        self.actions_battery_lvl.append( Action((lambda x: x < 50) , self.battery , 'less_50' , type = "less"))
        self.actions_battery_lvl.append( Action((lambda x: x > 90) , self.battery , 'more_90' , type = "less"))
        self.actions_plug.append( Action((lambda x: x == True ) , self.pluged , 'plug_on' , type = "less"))
        self.actions_plug.append( Action((lambda x: x == False) , self.pluged , 'plug_off' , type = "less"))



    def listen(self):
        ''' Main method! Here it loops! '''
        while True:
            # Get battery readings
            self.check_actions(actions_plug , self.pluged)
            self.check_actions(actions_battery_lvl , self.battery)

            # CPU unload
            time.sleep(time_to_skip)

    def check_actions(actions_array, arg):
        for action in actions_array:
            if action.check(arg):
                self.say(action.topic)


    def update_battery(self):
        self.battery = psutil.sensors_battery()
        self.pluged = self.battery.power_plugged
        return self.battery

    def enable_pyttsx3(self):
        import pyttsx3
        engine = pyttsx3.init()
    def enable_gTTS(self):
        from gtts import gTTS

    def say(self,topic):
        phrase = random.choice(self.config.phrases[topic])
        if self.config.voice_mode == 'gTTS':
            if self.is_connected():
                tts = gTTS(text=phrase, lang='en')
                tts.save("phrase.mp3")
                os.system("mpg123 phrase.mp3")
                os.system("rm phrase.mp3")
        else:
            engine.say(phrase)
            engine.runAndWait()
    def is_connected(self):
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection(("1.1.1.1", 53))
            return True
        except OSError:
            pass
        return False

class Action():
    """Class for templating actions.
    'Swich' type just swich back and forth.
    'less' type triggers when less then once"""
    def __init__(self, func , args0 , topic , type = "swich" ):
        self.func = func
        self.type = type
        self.base_flag = self.func(args0)
        self.topic = topic

    def check(self,args):
        if self.type == "swich":
            if self.func(args) != self.base_flag:
                self.base_flag = self.func(args)
                return True
            else:
                return False
        if self.type =="less":
            if self.func(args) == True:
                if self.base_flag == False:
                    self.base_flag = True
                    return True
                else: return False
            else:
                self.base_flag = False
                return False



if __name__ ==  '__main__':
    #Case direct call
    chatter = Chatter(Config())
