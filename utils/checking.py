"""Методы для проверки запросов"""
import json


class Cheking():

    """Метод для проверки статуса-кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")


    """Метод для проверки наличия полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        field = json.loads(result.text)
        assert list(field) == expected_value, 'ОШИБКА, Список полей не совпадает'
        print(list(field))
        print("Все поля присутствуют")


    """Метод для проверки значения обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name_1, field_name_2, expected_value):
        check = result.json()
        check_for_info = check.get(field_name_1)
        check_info = check_for_info.get(field_name_2)
        assert check_info == expected_value
        print(check_info)
        print(f"{field_name_2} верно!")


    @staticmethod
    def comparing_values_two_fields(result_m, result_f, field_name):
        """Метод для сравнения значений обязательных полей в ответах двух запросов"""
        check_m = result_m.json()
        check_info_m = check_m.get(field_name)
        check_f = result_f.json()
        check_info_f = check_f.get(field_name)
        assert check_info_m == check_info_f, "Ошибка, значение поля в запросах разное"
        print(f"Значения поля {field_name} в обоих запросах одинаковы")




