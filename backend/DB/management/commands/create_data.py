from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from DB.models import *
from DB.management.Classes.Catalogs.Catalogs import CatalogsCreator
from DB.management.Classes.Catalogs.SubCatalogs import SubCatalogCreator
from DB.management.Classes.Product.Product import ProductCreator
from DB.management.Classes.Additions.Tags import TagsCreator
from DB.management.Classes.Product.ProductInfo import ProductInfoCreator
from DB.management.Classes.Additions.Color import ColorCreator
from DB.management.Classes.Additions.Size import SizeCreator
from DB.management.Classes.Additions.image import ProductImageCreator
from DB.management.Classes.Order.face import OrderFaceCreator
from DB.management.Classes.Order.type import OrderTypeCreator
from DB.management.Classes.Order.payment import PaymentTypeCreator
from DB.management.Classes.Slider.slider import SliderCreator
from DB.management.Classes.Info.info import InfoSiteCreator
from icecream import ic


class Command(BaseCommand):
    help = "Create test data"

    def handle(self, *args, **options):
        User = get_user_model()
        try:
            User.objects.create_superuser(
                username="admin",
                email="admin@admin.ru",
                password="admin",
                first_name="admin",
                last_name="admin",
            )
        except Exception as e:
            pass

        try:
            Group.objects.create(name="Менеджеры")
            Group.objects.create(name="Подписчики")
        except Exception as e:
            pass

        try:
            Group.objects.get(name="Менеджеры").user_set.add(
                User.objects.get(username="admin")
            )
        except Exception as e:
            pass
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

        image_creator = ProductImageCreator("media/TestDataImage")
        image_creator.create(
            [
                "1.jpg",
                "2.jpg",
                "3.jpg",
                "4.jpg",
                "5.jpg",
                "6.jpg",
                "7.jpg",
                "8.jpg",
                "9.jpg",
                "10.jpg",
            ]
        )

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

        image_creator = ProductImageCreator("media/TestDataImage")
        image_creator.create(
            [
                "1.jpg",
                "2.jpg",
                "3.jpg",
                "4.jpg",
                "5.jpg",
                "6.jpg",
                "7.jpg",
                "8.jpg",
                "9.jpg",
                "10.jpg",
            ]
        )

        try:
            slider_creator = SliderCreator()
            slider_creator.create()
        except Exception as e:
            pass

        info_creator = InfoSiteCreator()
        info_creator.create_contact()
        info_creator.create_social()

        self.stdout.write(self.style.SUCCESS("Successfully created test data"))
