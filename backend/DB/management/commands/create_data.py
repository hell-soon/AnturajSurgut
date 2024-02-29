from django.core.management.base import BaseCommand
from DB.models import *
from DB.management.Classes.Catalogs.Catalogs import CatalogsCreator
from DB.management.Classes.Catalogs.SubCatalogs import SubCatalogCreator
from DB.management.Classes.Product.Product import ProductCreator
from DB.management.Classes.Additions.Tags import TagsCreator
from DB.management.Classes.Product.ProductInfo import ProductInfoCreator
from DB.management.Classes.Additions.Color import ColorCreator
from DB.management.Classes.Additions.Size import SizeCreator
from icecream import ic


class Command(BaseCommand):
    help = "Create test data"

    def handle(self, *args, **options):
        # ... Создание остальных моделей ...

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

        self.stdout.write(self.style.SUCCESS("Successfully created test data"))
