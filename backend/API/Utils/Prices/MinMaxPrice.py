from DB.models import ProductInfo
from django.db.models import Min, Max


def calculated_range_cost():
    first_data = ProductInfo.objects.filter(
        product__product_status=True, promotion=False
    ).aggregate(min_cost=Min("cost"), max_cost=Max("cost"))

    second_data = ProductInfo.objects.filter(
        product__product_status=True, promotion=True
    ).aggregate(
        min_promotion_cost=Min("promotion_cost"),
        max_promotion_cost=Max("promotion_cost"),
    )

    cost_range = {
        "min": min(first_data["min_cost"], second_data["min_promotion_cost"]),
        "max": max(first_data["max_cost"], second_data["max_promotion_cost"]),
    }

    return cost_range
