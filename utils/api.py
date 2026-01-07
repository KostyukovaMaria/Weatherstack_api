from utils.http_metods import Http_methods
"""Методы для тестирования Weatherstack"""


base_url = 'http://api.weatherstack.com' # Базовая URL
key = '?access_key=7a5af1a98d34e05c9740f43f7b068d01' #параметр  для всех запросов
query = 'Kaliningrad'     # местоположение для определения погоды(данный параметр можно менять)

class Weatherstack_api():

    """Метод для получения данных о погоде в режиме реального времени для указанных мест в градусах"""
    @staticmethod
    def get_weather_m():
        get_resource = '/current'      # ресурс для получения данных о погоде в режиме реального времени
        units_m = 'm'  # единицы измерения в градусах цельсия
        get_url = base_url + get_resource + key + '&query=' + query + '&units=' + units_m
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для получения данных о погоде в режиме реального времени для указанных мест в фаренгейтах"""

    @staticmethod
    def get_weather_f():
        get_resource = '/current'  # ресурс для получения данных о погоде в режиме реального времени
        units_f = 'f'  # единицы измерения в фаренгейтах
        get_url = base_url + get_resource + key + '&query=' + query + '&units=' + units_f
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get




