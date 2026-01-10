
import time
import allure
from utils.api import query
from utils.api import WeatherstackApi
from utils.checking import Checking
from utils.checking_date import CheckingDate
from utils.checking_temperature import CheckingTemrerature

@allure.epic("Test get weather")
class TestGetWeather():
    """Получения данных о погоде в режиме реального времени в градусах """
    @allure.description("Getting weather data for a random city in different units of measurement")
    def test_get_weather(self):

        print("Meтод GET в градусах")
        result_get_degrees = WeatherstackApi.get_weather_degrees()
        Checking.check_status_code(result_get_degrees, 200)
        Checking.checking_for_fields(result_get_degrees, ['request', 'location', 'current'])
        Checking.checking_field_values(result_get_degrees, 'location', 'name', query)
        CheckingDate.check_date(result_get_degrees, 'location', "localtime")
        CheckingDate.check_format_datetime(result_get_degrees, 'location', "localtime")

        print("Meтод GET в фаренгейтах")
        time.sleep(10) # необходимо добавить задержку времени из-за превышения скорости передачи запросов к API
        result_get_fahrenheit = WeatherstackApi.get_weather_fahrenheit()
        Checking.check_status_code(result_get_fahrenheit, 200)
        Checking.checking_for_fields(result_get_fahrenheit, ['request', 'location', 'current'])
        Checking.checking_field_values(result_get_fahrenheit, 'location', 'name', query)
        CheckingDate.check_date(result_get_fahrenheit, 'location', "localtime")
        CheckingDate.check_format_datetime(result_get_fahrenheit, 'location', "localtime")

        print("Сравнение двух запросов")
        CheckingTemrerature.check_temperature(result_get_degrees, result_get_fahrenheit, 'current', "temperature")
        Checking.comparing_values_two_fields(result_get_degrees, result_get_fahrenheit, 'location')


        print("Тестирование получения данных о погоде в режиме реального времени прошло успешно !!!")
