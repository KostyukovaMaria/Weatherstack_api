import requests


class Http_methods:
    """Класс по хранению HTTP методов"""

    headers = {'x-api-key': 'reqres_212c4f703e1d42289b91468911426546'}  # Заголовки нашего проекта
    cookie = ""  # Куки нашего проекта

    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result