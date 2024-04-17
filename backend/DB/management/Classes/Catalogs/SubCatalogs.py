from DB.models import SubCatalog
from DB.management.Utils.random_images import set_rangom_image


class SubCatalogCreator:
    def __init__(self, dir):
        self.dir = dir

    def create(self, catalogs):
        subCatalogs = []
        for item in catalogs:
            for i in range(0, 5):
                word = f"{item.name} {i+1}"
                subCatalogs.append(SubCatalog(name=word, catalog=item))

        data = SubCatalog.objects.bulk_create(subCatalogs)
        set_rangom_image(self.dir, data)
        return subCatalogs
