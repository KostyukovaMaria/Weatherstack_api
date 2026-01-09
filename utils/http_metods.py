import requests
from utils.consts import headers, cookie
class HttpMethods:
    """Класс по хранению HTTP методов"""

    @staticmethod
    def get(url):
        result = requests.get(url, headers=headers, cookies=cookie)
        return result

