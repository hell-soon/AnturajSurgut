import random
from DB.models import Compound

name = [
    "хлопок",
    "вискоза",
    "латекс",
    "полиэстер",
    "натуральная кожа",
    "шёлк",
    "поло",
    "кевлар",
    "винил",
    "полипропилен",
    "волокно акрила",
    "ламинат",
    "полиамид",
    "полистирол",
    "керамические блестки",
    "металлические блестки",
    "пластик",
    "натуральная шерсть",
    "натуральный каучук",
    "натуральный хут",
    "натуральный лён",
]


class CompoundCreator:
    def create(self):
        data = []
        for i in range(15):
            compaund = Compound(name=random.choice(name))
            data.append(compaund)

        data = Compound.objects.bulk_create(data)

        return data
