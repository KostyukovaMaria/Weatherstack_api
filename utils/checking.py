
import json

"""Методы для проверки запросов"""
class Checking():

    """Метод для проверки статуса-кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")


    """Метод для проверки наличия полей в ответе запроса"""
    @staticmethod
    def checking_for_fields(result, expected_value):
        field = json.loads(result.text)
        assert list(field) == expected_value, 'ОШИБКА, Список полей не совпадает'
        print(list(field))
        print("Все поля присутствуют")


    """Метод для проверки значения обязательных полей в ответе запроса"""
    @staticmethod
    def checking_field_values(result, field_name_1, field_name_2, expected_value):
        result_json = result.json()
        fild_value = result_json.get(field_name_1).get(field_name_2)
        assert fild_value == expected_value
        print(fild_value)
        print(f"{field_name_2} верно!")


    @staticmethod
    def comparing_values_two_fields(result_degrees, result_fahrenheit, field_name):
        """Метод для сравнения значений обязательных полей в ответах двух запросов"""
        result_json_degrees = result_degrees.json()
        fild_value_degrees = result_json_degrees.get(field_name)
        result_json_fahrenheit = result_fahrenheit.json()
        fild_value_fahrenheit = result_json_fahrenheit.get(field_name)
        assert fild_value_degrees == fild_value_fahrenheit, "Ошибка, значение поля в запросах разное"
        print(f"Значения поля {field_name} в обоих запросах одинаковы")







