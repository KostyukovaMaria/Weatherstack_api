
import time
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
            attempt = 0
            max_retries = 10
            retry_delay = 2
            while attempt < max_retries:
                try:
                    result = requests.get(url, headers=headers, cookies=cookie)
                    if result.status_code == 200:
                        break
                    else:
                        time.sleep(retry_delay)
                        attempt += 1
                except requests.exceptions.RequestException:
                    time.sleep(retry_delay)
                    attempt += 1
            Logger.add_response(result)
            return result



