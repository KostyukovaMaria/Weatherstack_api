
import allure
import requests
from utils.consts import headers, cookie
from utils.logger import Logger
class HttpMethods:
    """Класс по хранению HTTP методов"""

    @staticmethod
    def get(url):
        with allure.step("Get"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=headers, cookies=cookie)
            Logger.add_response(result)
            return result
