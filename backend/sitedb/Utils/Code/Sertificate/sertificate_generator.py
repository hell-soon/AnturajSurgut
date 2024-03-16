import random
import string


def generate_certificate_code(length=20):
    # Символы, которые могут быть использованы в коде сертификата
    characters = string.ascii_letters + string.digits
    # Генерация кода сертификата
    code = "".join(random.choice(characters) for _ in range(length))
    return code
