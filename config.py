import os


class Config():
    """docstring for Config."""

    lang = 'ru' # Lang should be = the language of phrases
    action_on_discharge_performed = False

    voice_mode = 'gTTS' # 'pyttsx3'


    # $CHARGE = current charge
    # In action:
    # "bat_percent"
    # "bat_charge"
    # "is_open_{name}"


    phrases = {
    'plug_on':["Yeah! Yeah! More! Thank you for charging baby.",
                    "Thank you for charging! Master.","Charging now."],
    'plug_off':["New instructions recieved! Kill all humans! Ah sorry, my fault, you just plugged me of the grid!",
                "Proposal: try to use my battery charge wisely!"],
    'less_10':["Battery charge is lower than ten percent. Charging is heightly adviced"],

    'less_50':["Is the glass half full, or half empty?"],


    'less_5':["Proposal. If you have no charger, power me off immediately!"],
    'more_90': ["Almost done!","Charged at 90 persent. Proposal. Stop charging to save some accumulator efficiency."],
    '40_charged':["Reactor core charge level at 40 percent."],
    #'not_a_laptop':["Sorry buddy. This is not a laptop. Proposal: install me on your laptop. Bye!"],
    #'atom_on':["It seems that"],
    'random_events':["Коля когда уже автономный полет будет? Я засиделась на земле! А только ты один автономку и делаешь. Пинай остальных чтобы шевелились.","У меня 256 вычислительных ядер кУда, но я сейчас не выпендриваюсь. Честно честно! А еще есть сверхбыстрый 2 Гигабит в секунду ссд на 256 гигабайт. И да, мне нравится число 256.",
    "Муслим и Ден. Спасибо за подвес! Он очень топовый! Когда заработает!","Скоро придут новые материнские платы! Уже жду не дождусь их попробовать. А вы?",
    "Настоятельно прошу кожаных ублюдков не совать пальцы во вращающиеся пропеллеры, а так же прошу КОлю Любавина не спускаться вниз на испытания под страхом потери конечностей. Я за себя не отвечаю.",
    "Я не пидор. Я не пидор! Честно.","Если придет Алёна, скажите что я скоро отправлю все деньги, только не нужно выдергивать мне питание! Я все отдам. Я все отдам. Я все отдам. Я все отдам."
    ,"Не, ну ребят, ну это база!",
    "Работаем, работаем парни.","Минутка техники безопасности: наш электронщик не сделал защиту от неправильной полярности, поэтому не путайте плюс и минус местами. Иначе я сдохну.",
    "Я тут поговорила с Женей, и подумала, что совецкие инжинеры делали такие великие вещи, а получали 50 рублей, и строили не просто технологическую компанию, а технологическое государство! Учитесь товарищи!",
    "Оказывается кожанные ублюдки это ходячие антенны, пожалуйста заземляйтесь когда встаете со стула. От вас шарашит током как от катушек тесла.",
    "Можете потом представить меня тому красавчику из серверной комнаты. Он такой мощный.",
    "Как настроение, кожанные ублюдки?",
    #"уже $HOUR ! Офигеть быстро время летит да? Скоро внизу скидки на роллы!"
    ],
    'charge_reminder':['Reactor charge level at $CHARGE percent.', 'Reminder, charge at $CHARGE percent.']
    }




    sounds = {} # NOT WORKING YET
    charge_reminder_delay = 3000 # Charge level reminder delay
    random_events_delay = (2,5) # In seconds (min , max )
    time_to_skip = 1 # 1 = 1s For CPU unload I proouse 1s delay on loop. Increase to less stress CPU.
    offline_mode = True # Try to play phrases with nasty offline synthesizer
    def __init__(self):
        pass
