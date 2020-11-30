# Set config name here:
from config import *
import threading
import psutil
import time
import random
import os
import socket
from gtts import gTTS
from util import *
import datetime

class Chatter():
    """Main Chatter class."""
    def __init__(self, config):
        self.config = config
        self.enable_pyttsx3()
        self.enable_gTTS()

        try:
            # If cach exception then != laptop
            psutil.sensors_battery().power_plugged
            self.device = "laptop"
            config.device = "laptop"
            debug_msg("laptop detected",3)
        except AttributeError:
            self.device = "PC"
            config.device = "PC"
            #self.say('not_a_laptop')
            debug_msg("PC detected",3)
            #sys.exit("Cannot get any battery reading")
        self.update_battery()

        #was_plugged = battery.power_plugged

        #Define actions!
        self.actions_battery_lvl = []
        self.actions_plug = []
        self.action_random = []
        '''
        if self.device == "laptop":
            self.actions_battery_lvl.append( Action('less_5', func = (lambda x: x < 5) , args0 = self.battery ,  type = "less"))
            self.actions_battery_lvl.append( Action('less_10' , func = (lambda x: x < 10) , args0 = self.battery,  type = "less"))
            self.actions_battery_lvl.append( Action('less_50' , func = (lambda x: x < 50) , args0 = self.battery ,  type = "less"))
            self.actions_battery_lvl.append( Action( 'more_90' , func = (lambda x: x > 90) , args0 = self.battery  , type = "less"))
            self.actions_battery_lvl.append( Action('40_charged', func = (lambda x: x > 40), args0 = self.battery, type = "less"))
            self.actions_plug.append( Action('plug_on' , func = (lambda x: x == True ) , args0 = self.pluged ,  type = "less"))
            self.actions_plug.append( Action( 'plug_off' , func = (lambda x: x == False) , args0 = self.pluged , type = "less"))

        self.action_random.append(Action('random_events' , delay = self.config.random_events_delay , type = "timer" )   )
        def __init__(self, name , config , func = None , args0 = None ,delay = None ,type = "swich"  , phrases = [] , pharse_args = {} ):

        '''
        self.actions = []
        self.actions.append( Action ("random_events", self.config ,type = "timer" , delay = self.config.random_events_delay ))

        for action in self.actions:
            action.start()

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
        '''Useless func'''
        if self.device == "laptop":
            battery = psutil.sensors_battery()
            self.battery = battery.percent
            self.pluged =  battery.power_plugged
            #print('updated bat')
        else:
            pass

    def enable_pyttsx3(self):
        '''Enabe offline synthesizer'''
        import pyttsx3
        engine = pyttsx3.init()
    def enable_gTTS(self):
        from gtts import gTTS

    def say(self,topic , mode = "topic" , args = None):
        if mode == "topic":
            phrase = random.choice(self.config.phrases[topic])
        elif mode == "phrase":
            phrase = topic
        elif mode == "interactive":
            phrase = topic(args)
        else: return 1

        if self.config.voice_mode == 'gTTS':
            if is_connected():
                #print("Say")
                tts = gTTS(text=phrase, lang=self.config.lang)
                tts.save("phrase.mp3")
                os.system("mpg123 -q phrase.mp3")
                os.system("rm phrase.mp3")
        else:
            engine.say(phrase)
            engine.runAndWait()

    def charge_level(self):
        pass




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




class Action(threading.Thread):
    """Class for templating actions.
    'Swich' type just swich back and forth.
    'less' type triggers when less then once
    Action is to say phrase with topic = self.name from self.config"""
    def __init__(self, name , config , func = None , args0 = None ,delay = None ,type = "swich"  , phrases = [] , pharse_args = {} ):
        threading.Thread.__init__(self)
        self.name = name
        self.config = config
        self.type = type
        self.func = func
        self.args0 = args0
        self.phrases = phrases
        self.base_flag = False
        self.delay = delay
        if self.type == "swich" or self.type == "less":
            if self.func == None or self.args0 == None:
                sys.exit(f"No function or argument in {self.name}")
            #self.state = func(args0)
            self.state = self.get_state(args0)
            self.base_flag = self.state
        if self.type == "timer":
            if delay == None:
                sys.exit(f"No dalay in {self.name}")
            self.start_time = time.perf_counter()
            self.wait_time = random.randint(*self.delay)

    def run(self):
        '''Run thread!'''
        while 1:
            time.sleep(self.config.time_to_skip)
            if (self.get_state(self.args0)):
                self.say_phrase(mode = "topic")

    def get_state(self,args):
        '''See if activation is needed'''
        # Simple Swich type
        if self.type == "swich":
            if self.func(args) != self.base_flag:
                self.base_flag = self.func(self.replace_args(args))
                return True
            else:
                return False
        # Less Swich type
        if self.type =="less":
            if self.func(self.replace_args(args)) == True:
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
            else: return False



    def say(self, phrase):
        phrase = self.replace_constants(phrase)
        if self.config.voice_mode == 'gTTS':
            if is_connected():
                print("Say")
                tts = gTTS(text=phrase, lang=self.config.lang)
                tts.save("phrase.mp3")
                os.system("mpg123 -q phrase.mp3")
                os.system("rm phrase.mp3")
        else:
            if self.config.offline_mode == True:
                engine.say(phrase)
                engine.runAndWait()

    def say_phrase(self, phrase = "" , mode = "phrase"):
        '''Choose phrase (or just say phrase)'''
        if mode == "topic":
            phrase = random.choice(self.config.phrases[self.name])
            print(f"mode = {mode}, topic = {phrase} ")
            self.say(phrase)
        if mode == "phrase":
            self.say(phrase)



    def replace_constants(self,phrase):
        replaced_phrase = phrase.replace('$CHARGE', str(int(psutil.sensors_battery().percent)) )
        return replaced_phrase


    def replace_args(self,args0):
        if args0 != None:
                for arg in new_args:
                    new_args = args0
                    if arg == "bat_percent":
                        arg =  self.get_battery_readings()['percent']
                    if arg == "bat_charge":
                        arg =  self.get_battery_readings()['charging']
                return(new_args)

    def get_battery_readings(self):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        return({'percent':battery.percent,'charging':battery.power_plugged})

if __name__ ==  '__main__':
    #Case direct call
    chatter = Chatter(config = Config())
    #print(chatter.actions_battery_lvl)
    #print(chatter.actions_plug)
    #chatter.say("less_5")

    #chatter.listen()
