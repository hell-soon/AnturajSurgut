from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, OrderItems


@receiver(post_save, sender=Order)
def upd_product_rating_quantity(sender, instance, **kwargs):
    if instance.order_status == "6":
        order_items = OrderItems.objects.filter(order=instance)
        for order_item in order_items:
            order_item.product.product.rating += order_item.quantity
            order_item.product.product.save()


@receiver(post_save, sender=Order)
def cancel_order(sender, instance, **kwargs):
    if instance.order_status == "5":
        order_items = OrderItems.objects.filter(order=instance)
        for order_item in order_items:
            order_item.product.quantity += order_item.quantity
            order_item.product.save()
