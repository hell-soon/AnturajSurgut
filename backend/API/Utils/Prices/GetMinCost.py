from django.db.models import Min
from DB.models import ProductInfo


def get_min_cost(product_id):
    min_regular_price = ProductInfo.objects.filter(product_id=product_id).aggregate(
        Min("cost")
    )["cost__min"]
    min_promotion_price = ProductInfo.objects.filter(
        product_id=product_id, promotion=True
    ).aggregate(Min("promotion_cost"))["promotion_cost__min"]

    if min_promotion_price and min_promotion_price < min_regular_price:
        return round(min_promotion_price)
    else:
        return round(min_regular_price)
