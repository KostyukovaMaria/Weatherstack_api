
import random
from utils.http_metods import HttpMethods
from utils.consts import base_url, key, all_query, get_resource, units_degrees, units_fahrenheit

"""Методы для тестирования Weatherstack"""
query = random.choice(all_query)
class WeatherstackApi():


    """Метод для получения данных о погоде в режиме реального времени для указанных мест в градусах"""
    @staticmethod
    def get_weather_degrees():
        get_url = base_url + get_resource + key + '&query=' + query + '&units=' + units_degrees
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для получения данных о погоде в режиме реального времени для указанных мест в фаренгейтах"""
    @staticmethod
    def get_weather_fahrenheit():
        get_url = base_url + get_resource + key + '&query=' + query + '&units=' + units_fahrenheit
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get








