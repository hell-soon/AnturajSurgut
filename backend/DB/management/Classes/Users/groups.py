from django.contrib.auth.models import Group


class GroupCreator:
    def create():
        groups = [
            Group(name="Администратор"),
            Group(name="Подписчик"),
            Group(name="Пользователь"),
        ]
        Group.objects.bulk_create(groups)
        return groups
