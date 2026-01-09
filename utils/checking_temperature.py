


class CheckingTemrerature():
    """Метод для сравнения температур двух запросов в разных единицах измерения"""

    @staticmethod
    def check_temperature(result_degrees, result_fahrenheit, field_name_1, field_name_2):
        """Метод для сравнения значений температур в градусах и в фаренгейтах обязательных полей в ответах запросов"""
        check_degrees = result_degrees.json()
        check_info_degrees = check_degrees.get(field_name_1).get(field_name_2)
        check_fahrenheit = result_fahrenheit.json()
        check_info_fahrenheit = check_fahrenheit.get(field_name_1).get(field_name_2)
        translation_check_info_fahrenheit = round((check_info_fahrenheit - 32) / 1.8)
        assert check_info_degrees == translation_check_info_fahrenheit
        print("Сравнение теператур в градусах и в фаренгейтах прошло успешно")


