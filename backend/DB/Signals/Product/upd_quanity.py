from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order


@receiver(post_save, sender=Order)
def cancel_order(sender, instance, **kwargs):
    if instance.order_status == "5":
        order_items = instance.orderitems_set.all()
        for order_item in order_items:
            order_item.product.quantity += order_item.quantity
            order_item.product.save()
