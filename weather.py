import config
import pyowm
from pyowm.utils.config import get_default_config


def get_weath(message):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = pyowm.OWM(config.API_WEATHER)

    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        print(temp)
        stat = w.status
        print(stat)
        answer = "В городе <b>" + message.text + "</b> сейчас " + w.detailed_status + "\n"
        print(answer)
        hum = w.humidity
        print(hum)
        time = w.reference_time(timeformat='iso')

        wind = w.wind()["speed"]
        print(wind)
        answer += "Температура в районе <b>" + str(temp) + "°C</b>\nСкорость ветра: <b>" + str(
            wind) + "м/с</b>" + "\n" + "Влажность: <b>" + str(hum) + "%</b>" + "\n" + "Время: " + str(time) + "\n"

        if temp < 0:
            answer += "Сейчас холодно, лучше одеться потеплее."
        elif temp < 15:
            answer += "Сейчас прохладно, не забудь курточку."
        elif temp > 25:
            answer += "Жарковато, не забудь водичку."
        else:
            answer += "Температура в норме, в принципе, жить можно!"
        print(answer)
        return answer

    except Exception:
        answer = 'Ошибка! Город не найден.'
        print(message.text)
        return answer
