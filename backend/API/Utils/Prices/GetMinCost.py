from django.db.models import Min
from DB.models import ProductInfo


def get_min_cost(product_id):
    min_regular_price = ProductInfo.objects.filter(product_id=product_id).aggregate(
        Min("cost")
    )["cost__min"]
    min_promotion_price = ProductInfo.objects.filter(
        product_id=product_id, promotion=True
    ).aggregate(Min("promotion_cost"))["promotion_cost__min"]

    if min_regular_price is not None and min_promotion_price is not None:
        return (
            round(min_promotion_price)
            if min_promotion_price < min_regular_price
            else round(min_regular_price)
        )
    elif min_promotion_price is not None:
        return round(min_promotion_price)
    elif min_regular_price is not None:

        return round(min_regular_price)
    else:
        return None
