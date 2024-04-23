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
from DB.management.Classes.Additions.image import ProductImageCreator
from DB.management.Classes.Order.face import OrderFaceCreator
from DB.management.Classes.Order.type import OrderTypeCreator
from DB.management.Classes.Order.payment import PaymentTypeCreator
from DB.management.Classes.Slider.slider import SliderCreator
from DB.management.Classes.Info.info import InfoSiteCreator
from DB.management.Classes.Users.admin import AdminsCreator
from DB.management.Classes.Users.groups import GroupCreator
from DB.management.Classes.Reviews.Reviews import ReviewsCreator
from DB.management.Classes.Additions.Compound import CompoundCreator
from DB.management.Classes.Order.status import StatusCreator


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

        compaund_creator = CompoundCreator()
        compaunds = compaund_creator.create()

        product_creator = ProductCreator()
        products = product_creator.create(sub_catalogs, tags, compaunds)

        productinfo_creator = ProductInfoCreator()
        productinfo_creator.create(products, colors, size)

        order_face_creator = OrderFaceCreator()
        order_face_creator.create()

        order_type_creator = OrderTypeCreator()
        order_type_creator.create()

        order_status_creator = StatusCreator()
        order_status_creator.create()

        payment_type_creator = PaymentTypeCreator()
        payment_type_creator.create()

        slider_creator = SliderCreator(test_data_dir)
        slider_creator.create()

        info_creator = InfoSiteCreator()
        data = info_creator.create_pk()
        info_creator.create_contact(data)
        info_creator.create_social(data)

        # Use this because celery in docker depence_on: - backend_container
        try:

            admin_creator = AdminsCreator(User)
            created_admin = admin_creator.create()

            group_creator = GroupCreator()
            groups = group_creator.create()
        except Exception as e:
            pass

        reviews_creator = ReviewsCreator()
        reviews_creator.create()

        self.stdout.write(self.style.SUCCESS("Successfully created test data"))
