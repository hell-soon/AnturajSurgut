from django.core.files import File
import os
import random


def set_rangom_image(dir, data):
    files = os.listdir(dir)
    for item in data:
        random_file = random.choice(files)
        with open(os.path.join(dir, random_file), "rb") as file:
            django_file = File(file)
            item.image.save(random_file, django_file, save=True)
