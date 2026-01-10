


class CheckingTemrerature():
    """Метод для сравнения температур двух запросов в разных единицах измерения"""

    @staticmethod
    def check_temperature(result_degrees, result_fahrenheit, field_name_1, field_name_2):
        """Метод для сравнения значений температур в градусах и в фаренгейтах обязательных полей в ответах запросов"""
        result_json_degrees = result_degrees.json()
        temperature_degrees = result_json_degrees.get(field_name_1).get(field_name_2)
        result_json_fahrenheit = result_fahrenheit.json()
        temperature_fahrenheit = result_json_fahrenheit.get(field_name_1).get(field_name_2)
        translation_temperature_fahrenheit = round((temperature_fahrenheit - 32) / 1.8)
        assert temperature_degrees == translation_temperature_fahrenheit
        print("Сравнение теператур в градусах и в фаренгейтах прошло успешно")





