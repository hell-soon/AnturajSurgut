from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order


@receiver(post_save, sender=Order)
def upd_product_rating_quantity(sender, instance, **kwargs):
    if instance.order_status == "6":
        order_items = instance.orderitems_set.all()
        for order_item in order_items:
            order_item.product.product.rating += order_item.quantity
            order_item.product.product.save()
