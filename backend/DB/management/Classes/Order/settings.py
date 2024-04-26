from order.models import OrderSettings


class SettingsCreator:
    def create(self):
        data = OrderSettings.objects.create(name="Настройки заказов")
        return data
