from django.db.models.signals import post_save
from django.dispatch import receiver
from DB.models import Product


@receiver(post_save, sender=Product)
def calculate_product_rating(sender, instance, **kwargs):
    # instance.rating = instance.calculate_rating()
    # instance.save(update_fields=["rating"])
    pass
