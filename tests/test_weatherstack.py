
import allure
from utils.api import query
from utils.api import WeatherstackApi
from utils.checking import Checking
from utils.checking_date import CheckingDate
from utils.checking_temperature import CheckingTemrerature

@allure.epic("Test get weather")
class TestGetWeatherData():

    @allure.description("Получения данных о погоде в режиме реального времени в градусах")
    def test_get_weather_data_in_degrees(self):
        with allure.step('Шаг 1: Отправить запроc для получения данных о погоде в градусах.'):
            result_get_degrees = WeatherstackApi.get_weather_degrees()
        with allure.step('Шаг 2: Проверка статус-кода ответа для запроса в градусах'):
            Checking.check_status_code(result_get_degrees, 200)
        with allure.step('Шаг 3: Проверка корректности названия полей из json-ответа в градусах'):
            Checking.checking_for_fields(result_get_degrees, ['request', 'location', 'current'])
        with allure.step('Шаг 4: Проверка на сответствие названия выбранного рандомным способом города и '
                         'названия города в поле из json-ответа в градусах'):
            Checking.checking_field_values(result_get_degrees, 'location', 'name', query)
        with allure.step('Шаг 5: Проверка соответствия реальной даты и времени с датой и временем из json-ответа в градусах'):
            CheckingDate.check_date(result_get_degrees, 'location', "localtime")
        with allure.step('Шаг 6: Проверка соответствия ожидаемого формата дата-время с форматом из json-ответа в градусах'):
            CheckingDate.check_format_datetime(result_get_degrees, 'location', "localtime")


    @allure.description("Получения данных о погоде в режиме реального времени в фаренгейтах")
    def test_get_weather_data_in_fahrenheit(self):

        with allure.step('Шаг 1: Отправить запроc для получения данных о погоде в фаренгейтах.'):
            result_get_fahrenheit = WeatherstackApi.get_weather_fahrenheit()
        with allure.step('Шаг 2: Проверка статус-кода ответа для запроса в фаренгейтах'):
            Checking.check_status_code(result_get_fahrenheit, 200)
        with allure.step('Шаг 3: Проверка корректности названия полей из json-ответа в фаренгейтах'):
            Checking.checking_for_fields(result_get_fahrenheit, ['request', 'location', 'current'])
        with allure.step('Шаг 4: Проверка на сответствие названия выбранного рандомным способом города и '
                         'названия города в поле из json-ответа в фаренгейтах'):
            Checking.checking_field_values(result_get_fahrenheit, 'location', 'name', query)
        with allure.step('Шаг 5: Проверка соответствия реальной даты и времени с датой и временем из json-ответа в фаренгейтах'):
            CheckingDate.check_date(result_get_fahrenheit, 'location', "localtime")
        with allure.step('Шаг 6: Проверка соответствия ожидаемого формата дата-время с форматом из json-ответа в фаренгейтах'):
            CheckingDate.check_format_datetime(result_get_fahrenheit, 'location', "localtime")



    @allure.description("Сравнение значений данных о погоде в фаренгейтах и в градусах")
    def test_comparison_of_weather_data_in_degrees_and_in_fahrenheit(self):
        with allure.step('Шаг 1: Отправить запроc для получения данных о погоде в градусах.'):
            result_get_degrees = WeatherstackApi.get_weather_degrees()
        with allure.step('Шаг 2: Отправить запроc для получения данных о погоде в фаренгейтах.'):
            result_get_fahrenheit = WeatherstackApi.get_weather_fahrenheit()
        with allure.step('Шаг 3: Сравнение значений температуры в градусах и температуры в фаренгейтах, переведенной в градусы'):
            CheckingTemrerature.comparing_temperatures_in_degrees_and_fahrenheit(result_get_degrees, result_get_fahrenheit, 'current', "temperature")
        with allure.step('Шаг 4: Проверка на сответствие названия города из json-ответа в градусах  и в фаренгейтах'):
            Checking.comparing_values_two_fields(result_get_degrees, result_get_fahrenheit, 'location')

