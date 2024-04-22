from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, OrderItems, OrderAddress


@receiver(post_save, sender=Order)
def upd_product_rating_quantity(sender, instance, **kwargs):
    if instance.order_status == "6":
        order_items = OrderItems.objects.filter(order=instance)
        for order_item in order_items:
            order_item.product.product.total_sales += order_item.quantity
            order_item.product.product.save()


@receiver(post_save, sender=Order)
def cancel_order(sender, instance, **kwargs):
    if instance.order_status == "5":
        order_items = OrderItems.objects.filter(order=instance)
        for order_item in order_items:
            order_item.product.quantity += order_item.quantity
            order_item.product.save()

    if instance.order_type.name == "Самовывоз":
        order_address, created = OrderAddress.objects.get_or_create(
            order=instance,
            city="Сургут",
            region="Ханты-Мансийский автономный округ — Югра",
            post_index="628406",
            floor=1,
            street="​Улица Иосифа Каролинского",
            house="13",
        )
        # Если запись была создана, сохраняем ее
        if created:
            order_address.save()
