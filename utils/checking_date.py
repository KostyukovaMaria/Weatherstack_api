
from datetime import datetime, timedelta
from utils.consts import upper_limit

class CheckingDate():
    """Методы для проверки обязательного поля запроса localtime """
    @staticmethod
    def check_date(result, field_name_1, field_name_2):
        """Метод для проверки значения даты обязательного поля в ответе запроса"""
        check = result.json()
        check_for_info = check.get(field_name_1).get(field_name_2)
        today_date = datetime.today()  # Получение текущей даты
        check_info_datetime = datetime.strptime(check_for_info, '%Y-%m-%d %H:%M')
        delta = abs(check_info_datetime - today_date)  # модуль разности дат из API и фактической
        timedelta_delta = today_date - (today_date - timedelta(minutes=upper_limit))  # переменная для сравнения равная 15 минутам
        assert delta < timedelta_delta, "Ошибка, дата + время некорректно"
        print("Проверка времени прошла успешно")

    @staticmethod
    def check_format_datetime(result, field_name_1, field_name_2):
        """Метод для проверки формата даты обязательного поля в ответе запроса"""
        check = result.json()
        check_for_info = check.get(field_name_1).get(field_name_2)
        expected_format = '%Y-%m-%d %H:%M'
        date_obj = datetime.strptime(check_for_info, expected_format)
        formated_str = date_obj.strftime(expected_format) # преобразование обратно в строку
        assert check_for_info == formated_str, 'ОШИБКА, Неверный формат даты'
        print("Формат даты корректен")














