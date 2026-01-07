import json
import time

from requests import Response

from utils.api import Weatherstack_api
from utils.checking import Checking
from utils.checking_date import Checking_date
from utils.checking_temperature import Checking_temrerature

class Test_get_weather():
    """Получения данных о погоде в режиме реального времени для Калининграда в градусах """
    def test_get_weather_m(self):

        print("Meтод GET в градусах")
        result_get_m = Weatherstack_api.get_weather_m()
        # check_get = result_get.json()
        # query = check_get.get("query")
        Checking.check_status_code(result_get_m, 200)
        Checking.check_json_token(result_get_m, ['request', 'location', 'current'])
        Checking.check_json_value(result_get_m, 'location', 'name', 'Kaliningrad')
        Checking_date.check_date(result_get_m, 'location', "localtime")
        Checking_date.check_format_datetime(result_get_m, 'location', "localtime")


        print("Meтод GET в фаренгейтах")
        time.sleep(10) # необходимо добавить задержку времени из-за превышения скорости передачи запросов к API
        result_get_f = Weatherstack_api.get_weather_f()
        Checking.check_status_code(result_get_f, 200)
        Checking.check_json_token(result_get_f, ['request', 'location', 'current'])
        Checking.check_json_value(result_get_f, 'location', 'name', 'Kaliningrad')
        Checking_date.check_date(result_get_f, 'location', "localtime")
        Checking_date.check_format_datetime(result_get_f, 'location', "localtime")
        Checking_temrerature.check_temrerature(result_get_m, result_get_f, 'current', "temperature")
        Checking.comparing_values_two_fields(result_get_m, result_get_f, 'location')


        print("Тестирование получения данных о погоде в режиме реального времени для Калининграда прошло успешно !!!")