class AdminsCreator:
    def __init__(self, user):
        self.user = user

    def create(self):
        admin = self.user.objects.create_superuser(
            username="admin",
            email="admin@admin.ru",
            password="admin",
            first_name="admin",
            last_name="admin",
        )

        return admin
