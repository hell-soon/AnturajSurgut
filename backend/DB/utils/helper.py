import re


def get_contact_info(user_communication):
    # Регулярное выражение для телефонных номеров и email-адресов
    phone_regex = r"\+7\s?\(?\d{3}\)?\s?\d{3}-?\d{2}-?\d{2}"
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    # Сначала ищем телефонные номера
    phones = re.findall(phone_regex, user_communication)
    if phones:
        return phones

    # Если телефонных номеров нет, ищем email-адреса
    emails = re.findall(email_regex, user_communication)
    if emails:
        return emails

    # Если ничего не найдено, возвращаем None TODO Отправка письма менеджерам с номером заказа
    return None
