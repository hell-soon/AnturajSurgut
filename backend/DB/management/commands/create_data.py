from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from DB.models import *
from DB.management.Classes.Catalogs.Catalogs import CatalogsCreator
from DB.management.Classes.Catalogs.SubCatalogs import SubCatalogCreator
from DB.management.Classes.Product.Product import ProductCreator
from DB.management.Classes.Additions.Tags import TagsCreator
from DB.management.Classes.Product.ProductInfo import ProductInfoCreator
from DB.management.Classes.Additions.Color import ColorCreator
from DB.management.Classes.Additions.Size import SizeCreator
from DB.management.Classes.Order.face import OrderFaceCreator
from DB.management.Classes.Order.type import OrderTypeCreator
from DB.management.Classes.Order.payment import PaymentTypeCreator
from icecream import ic


class Command(BaseCommand):
    help = "Create test data"

    def handle(self, *args, **options):
        User = get_user_model()

        User.objects.create_superuser(
            username="admin",
            email="admin@admin.ru",
            password="admin",
        )

        catalog_creator = CatalogsCreator()
        catalogs = catalog_creator.create()

        sub_catalog_creator = SubCatalogCreator()
        sub_catalogs = sub_catalog_creator.create(catalogs)

        tags_creator = TagsCreator()
        tags = tags_creator.create()

        colors_creator = ColorCreator()
        colors = colors_creator.create()

        size_creator = SizeCreator()
        size = size_creator.create()

        product_creator = ProductCreator()
        products = product_creator.create(sub_catalogs, tags)

        productinfo_creator = ProductInfoCreator()
        productinfo_creator.create(products, colors, size)

        order_face_creator = OrderFaceCreator()
        order_face_creator.create()

        order_type_creator = OrderTypeCreator()
        order_type_creator.create()

        payment_type_creator = PaymentTypeCreator()
        payment_type_creator.create()

        self.stdout.write(self.style.SUCCESS("Successfully created test data"))
