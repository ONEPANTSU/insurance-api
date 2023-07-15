get_all_rates_error = "Ошибка при получении информации о всех тарифах"
get_all_rates_success = (
    "Успешное получение информации о всех тарифах за {days_count} {days}"
)

get_rate_by_date_error = "Ошибка при получении информации о тарифах за {date}"
get_rate_by_date_success = "Успешное получение информации о тарифах за {date}"

get_rate_error = "Ошибка при получении информации о тарифе на {cargo_type} за {date}"
get_rate_success = "Успешное получение информации о тарифе на {cargo_type} за {date}"

add_rate_error = "Ошибка при добавлении тарифа на {cargo_type} за {date}"
add_rate_success = "Успешное добавление тарифа на {cargo_type} за {date}"

edit_rate_error = "Ошибка при изменении тарифа на {cargo_type} за {date}"
edit_rate_success = "Успешное изменение тарифа на {cargo_type} за {date}"

delete_rates_error = "Ошибка при удалении тарифов за {date}"
delete_rates_success = "Успешное удаление тарифов за {date}"

delete_rate_error = "Ошибка при удалении тарифа на {cargo_type} за {date}"
delete_rate_success = "Успешное удаление тарифа на {cargo_type} за {date}"

MESSAGE = {
    "get_all_rates_error": get_all_rates_error,
    "get_all_rates_success": get_all_rates_success,
    "get_rate_by_date_error": get_rate_by_date_error,
    "get_rate_by_date_success": get_rate_by_date_success,
    "get_rate_error": get_rate_error,
    "get_rate_success": get_rate_success,
    "add_rate_error": add_rate_error,
    "add_rate_success": add_rate_success,
    "edit_rate_error": edit_rate_error,
    "edit_rate_success": edit_rate_success,
    "delete_rates_error": delete_rates_error,
    "delete_rates_success": delete_rates_success,
    "delete_rate_error": delete_rate_error,
    "delete_rate_success": delete_rate_success,
}


def get_days_word(days_count: int):
    last_num = days_count % 10
    if last_num == 1:
        return "день"
    if 2 <= last_num <= 4:
        return "дня"
    else:
        return "дней"
