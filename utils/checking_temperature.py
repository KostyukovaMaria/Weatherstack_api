"""Метод для сравнения температур двух запросов в разных единицах измерения"""

class Cheking_temrerature():

    @staticmethod
    def check_temrerature(result_m, result_f, field_name_1, field_name_2):
        """Метод для сравнения значений температур в градусах и в фаренгейтах обязательных полей в ответах запросов"""
        check_m = result_m.json()
        check_for_info_m = check_m.get(field_name_1)
        check_info_m = check_for_info_m.get(field_name_2) #получение значения температуры в градусах
        check_f = result_f.json()
        check_for_info_f = check_f.get(field_name_1)
        check_info_f = check_for_info_f.get(field_name_2)  # получение значения температуры в фаренгейтах
        translation_check_info_f = round((check_info_f - 32) / 1.8)
        assert check_info_m == translation_check_info_f
        print("Сравнение теператур в градусах и в фаренгейтах прошло успешно")