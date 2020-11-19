import os


class Config():
    """docstring for Config."""

    lang = 'en'
    action_on_discharge_performed = False

    voice_mode = 'gTTS' # 'pyttsx3'




    phrases = {
    'plug_on':["Yeah! Yeah! More! Thank you for charging baby.",
                    "Thank you for charging! Master.","Charging now."],
    'plug_off':["New instructions recieved! Kill all humans! Ah sorry, my fault, you just plugged me of the grid!",
                "Proposal: try to use my battery charge wisely!"],
    'less_10':["Battery charge is lower than ten percent. Charging is heightly adviced"],

    'less_50':["Is the glass half full, or half empty?"],


    'less_5':["Proposal. If you have no charger, power me off immediately!"],
    'more_90': ["Almost done!","Charged at 90 persent. Proposal. Stop charging to save some accumulator efficiency."],
    #'not_a_laptop':["Sorry buddy. This is not a laptop. Proposal: install me on your laptop. Bye!"],
    #'atom_on':["It seems that"],
    'random_events':["I'm still here and you are still amaizing!","Another day. Another problems to solve.","Sound check. Are you still there human?"]
    }

    random_events_delay = (1800,3600)
    time_to_skip = 1 # For CPU unload I proouse 1s delay on loop.

    def __init__(self):
        pass
