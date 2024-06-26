import random
import string
from django.apps import apps


def generate_certificate_code(block_length=4, blocks=4, separator="-"):
    # Символы, которые могут быть использованы в коде сертификата
    characters = string.ascii_letters + string.digits

    # Функция для генерации блока кода сертификата
    def generate_block(length):
        return "".join(random.choice(characters) for _ in range(length))

    code_blocks = [generate_block(block_length) for _ in range(blocks)]
    code = separator.join(code_blocks)

    return code


def generate_certificate():
    Sertificate = apps.get_model("sitedb", "Sertificate")

    while True:
        code = generate_certificate_code()
        if not Sertificate.objects.filter(code=code).exists():
            return code
