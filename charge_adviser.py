import pyttsx3
import psutil
import time



time_to_skip = 1


engine = pyttsx3.init()
battery = psutil.sensors_battery()

was_plugged = battery.power_plugged
action_on_discharge_performed = False

#voice_mode = 'gTTS' # 'pyttsx3'

if battery.percent > 50:
    battery_low = False



while True:
    # Get battery readings
    battery = psutil.sensors_battery()
    if was_plugged != battery.power_plugged:
        if was_plugged == False:
            was_plugged = battery.power_plugged
            # Plug in action!
            say("Thank you for charging.")
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
    if battery.percent = 100 :
        pass
    if battery_low == False:
        if  battery.percent <= 50:
            say("")


    # CPU unload
    time.sleep(time_to_skip)


def say(sent):
    if
        engine.say(sent)
        engine.runAndWait()
