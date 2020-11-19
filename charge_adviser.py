# Set config name here:
from config import *

import psutil
import time
import random
import os
import socket
from gtts import gTTS
from util import *


class Chatter():
    """Main Chatter class."""
    def __init__(self, config):
        self.config = config

        self.enable_pyttsx3()
        self.enable_gTTS()

        try:
            psutil.sensors_battery().power_plugged
            self.device = "laptop"
        except AttributeError:
            self.device = "PC"
            #self.say('not_a_laptop')
            debug_msg("PC detected",0)
            #sys.exit("Cannot get any battery reading")
        self.update_battery()

        #was_plugged = battery.power_plugged

        #Define actions!
        self.actions_battery_lvl = []
        self.actions_plug = []
        self.action_random = []

        if self.device == "laptop":
            self.actions_battery_lvl.append( Action('less_5', func = (lambda x: x < 5) , args0 = self.battery ,  type = "less"))
            self.actions_battery_lvl.append( Action('less_10' , func = (lambda x: x < 10) , args0 = self.battery,  type = "less"))
            self.actions_battery_lvl.append( Action('less_50' , func = (lambda x: x < 50) , args0 = self.battery ,  type = "less"))
            self.actions_battery_lvl.append( Action( 'more_90' , func = (lambda x: x > 90) , args0 = self.battery  , type = "less"))
            self.actions_plug.append( Action('plug_on' , func = (lambda x: x == True ) , args0 = self.pluged ,  type = "less"))
            self.actions_plug.append( Action( 'plug_off' , func = (lambda x: x == False) , args0 = self.pluged , type = "less"))

        self.action_random.append(Action('random_events' , delay = self.config.random_events_delay , type = "timer" )   )




    def listen(self):
        ''' Main method! Here it loops! '''
        while True:
            self.update_battery()
            #print(self.pluged)
            #print(self.battery)
            # Get battery readings
            if self.device == "laptop":
                self.check_actions(self.actions_plug , arg =self.pluged)
                self.check_actions(self.actions_battery_lvl ,arg = self.battery)
            self.check_actions(self.action_random)
            # CPU unload
            time.sleep(self.config.time_to_skip)

    def check_actions(self,actions_array, arg = None):
        for action in actions_array:
            if action.check(arg):
                #print(f"Check for {action.topic}")
                self.say(action.topic)


    def update_battery(self):
        if self.device == "laptop":
            battery = psutil.sensors_battery()
            self.battery = battery.percent
            self.pluged =  battery.power_plugged
            #print('updated bat')
        else:
            pass

    def enable_pyttsx3(self):
        import pyttsx3
        engine = pyttsx3.init()
    def enable_gTTS(self):
        from gtts import gTTS

    def say(self,topic , mode = "topic"):
        if mode == "topic":
            phrase = random.choice(self.config.phrases[topic])
        if mode == "phrase":
            phrase = topic
        else: return 1

        if self.config.voice_mode == 'gTTS':
            if self.is_connected():
                tts = gTTS(text=phrase, lang=self.config.lang)
                tts.save("phrase.mp3")
                os.system("mpg123 -q phrase.mp3")
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

    def check_sys(self):
        from sys import platform
        if platform == "linux" or platform == "linux2":
            #Linux
            self.platform = "linux"
        elif platform == "darwin":
            # OS X
            self.platform = "osx"
        elif platform == "win32":
            # Windows...
            self.platform = "windows"



class Action():
    """Class for templating actions.
    'Swich' type just swich back and forth.
    'less' type triggers when less then once"""
    def __init__(self, topic , func = None , args0 = None  ,type = "swich" , delay = None ):
        self.func = func
        self.args0 = args0
        self.type = type
        self.topic = topic


        if self.type == "timer":
            self.start_time = time.perf_counter()
            if delay == None:
                debug_msg(f"No delay set! In action = {self.topic}! Setting auto time",0)
                self.delay = (800,1200)
            self.delay = delay
            self.wait_time = random.randint(*self.delay)

        if self.type == "less" or self.type == "swich":
            if self.func == None:
                sys.exit(f"Function for {self.topic} not set even if type set as a swich type. Terminating!")
            elif ( self.args0 == None):
                sys.exit(f"Initial values for {self.topic} not set even if type set as a swich type. Terminating!")

            self.base_flag = self.func(args0)







    def check(self,args):
        if (self.type == "swich" or self.type == "less" ) and args == None:
            sys.exit(f"Initial values for {self.topic} not set even if type set as a swich type. Terminating!")
        # Simple Swich type
        if self.type == "swich":
            if self.func(args) != self.base_flag:
                self.base_flag = self.func(args)
                return True
            else:
                return False
        # Less Swich type
        if self.type =="less":
            if self.func(args) == True:
                if self.base_flag == False:
                    self.base_flag = True
                    return True
                else: return False
            else:
                self.base_flag = False
                return False
        # Timer type
        if self.type == "timer":
            if time.perf_counter() - self.start_time > self.wait_time:
                debug_msg(f"time is {time.perf_counter() - self.start_time} ", 10 )
                self.start_time = time.perf_counter()
                self.wait_time = random.randint(*self.delay)

                return True
            else:
                return False



if __name__ ==  '__main__':
    #Case direct call
    chatter = Chatter(config = Config())
    #print(chatter.actions_battery_lvl)
    #print(chatter.actions_plug)
    #chatter.say("less_5")

    chatter.listen()
