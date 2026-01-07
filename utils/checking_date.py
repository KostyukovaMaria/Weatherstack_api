"""Методы для проверки запросов"""
import json
from datetime import datetime, timedelta

class Cheking_date():

    @staticmethod
    def check_date(result, field_name_1, field_name_2):
        """Метод для проверки значения даты обязательного поля в ответе запроса"""
        check = result.json()
        check_for_info = check.get(field_name_1)
        check_info = check_for_info.get(field_name_2)
        today_date = datetime.today()  # Получение текущей даты
        new_date = today_date - timedelta(hours=1)  # получение корректного времени для Калининграда
        check_info_datetime = datetime.strptime(check_info, '%Y-%m-%d %H:%M')
        delta = abs(check_info_datetime - new_date)  # модуль разности дат из API и фактической
        timedelta_delta = today_date - (
                    today_date - timedelta(minutes=15))  # переменная для сравнения равная 15 минутам
        assert delta < timedelta_delta, "Ошибка, дата + время некорректно"
        print("Проверка времени прошла успешно")

    @staticmethod
    def check_format_datetime(result, field_name_1, field_name_2):
        """Метод для проверки формата даты обязательного поля в ответе запроса"""
        check = result.json()
        check_for_info = check.get(field_name_1)
        check_info = check_for_info.get(field_name_2)
        expected_format = '%Y-%m-%d %H:%M'
        date_obj = datetime.strptime(check_info, expected_format)
        formated_str = date_obj.strftime(expected_format) # преобразование обратно в строку
        assert check_info == formated_str, 'ОШИБКА, Неверный формат даты'
        print("Формат даты корректен")










