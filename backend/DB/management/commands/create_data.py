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
from DB.management.Classes.Users.admin import AdminsCreator
from DB.management.Classes.Users.groups import GroupCreator


class Command(BaseCommand):
    help = "Create test data"

    def handle(self, *args, **options):
        User = get_user_model()
        test_data_dir = "media/TestDataImage"
        catalog_creator = CatalogsCreator(test_data_dir)
        catalogs = catalog_creator.create()

        sub_catalog_creator = SubCatalogCreator(test_data_dir)
        sub_catalogs = sub_catalog_creator.create(catalogs)

        tags_creator = TagsCreator()
        tags = tags_creator.create()

        colors_creator = ColorCreator()
        colors = colors_creator.create()

        size_creator = SizeCreator()
        size = size_creator.create()

        image_creator = ProductImageCreator(test_data_dir)
        image_creator.create()

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

        slider_creator = SliderCreator(test_data_dir)
        slider_creator.create()

        info_creator = InfoSiteCreator()
        info_creator.create_contact()
        info_creator.create_social()

        # Use this because celery in docker depence_on: - backend_container
        try:
            admin_creator = AdminsCreator(User)
            admin = admin_creator.create()

            group_creator = GroupCreator()
            groups = group_creator.create()
        except Exception as e:
            pass

        self.stdout.write(self.style.SUCCESS("Successfully created test data"))
