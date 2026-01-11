


from datetime import datetime, timedelta
from utils.consts import upper_limit, expected_format

class CheckingDate():
    """Методы для проверки обязательного поля запроса localtime """
    @staticmethod
    def check_date(result, field_name_1, field_name_2):
        """Метод для проверки значения даты обязательного поля в ответе запроса"""
        result_json = result.json()
        value_date = result_json.get(field_name_1).get(field_name_2)
        today_date = datetime.today()  # Получение текущей даты
        value_date_datetime = datetime.strptime(value_date, '%Y-%m-%d %H:%M')
        delta = abs(value_date_datetime - today_date)  # модуль разности дат из API и фактической
        interval_comparison = today_date - (today_date - timedelta(minutes=upper_limit))  # переменная для сравнения равная 15 минутам
        assert delta < interval_comparison, "Ошибка, дата + время некорректно"
        print("Значение даты корректно")


    @staticmethod
    def check_format_datetime(result, field_name_1, field_name_2):
        """Метод для проверки формата даты обязательного поля в ответе запроса"""
        result_json = result.json()
        value_date = result_json.get(field_name_1).get(field_name_2)
        date_obj = datetime.strptime(value_date, expected_format)
        formated_date_obj = date_obj.strftime(expected_format) # преобразование обратно в строку
        assert value_date == formated_date_obj, 'ОШИБКА, Неверный формат даты'
        print("Формат даты корректный")








