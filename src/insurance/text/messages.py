insurance_request_error = "Произошла ошибка при расчёте стоимости страхования"
insurance_request_success = "Успешно расчитана стоимость страхования, результат записан в историю страхования в базе данных"

get_insurance_history_error = "Произошла ошибка при получении истории страхования"
get_insurance_history_success = (
    "Успешное получение истории страхования. Найденно {count} {rows}"
)

MESSAGE = {
    "insurance_request_error": insurance_request_error,
    "insurance_request_success": insurance_request_success,
    "get_insurance_history_success": get_insurance_history_success,
    "get_insurance_history_error": get_insurance_history_error,
}


def get_rows_word(rows_count: int):
    last_num = rows_count % 10
    if last_num == 1:
        return "запись"
    if 2 <= last_num <= 4:
        return "записи"
    else:
        return "записей"
