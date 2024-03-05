from DB.models import SubCatalog


class SubCatalogCreator:
    def create(self, catalogs):
        subCatalogs = [
            SubCatalog(name="Брюки", catalog=catalogs[4]),
            SubCatalog(name="Желетки", catalog=catalogs[4]),
            SubCatalog(name="Сарафаны", catalog=catalogs[4]),
            SubCatalog(name="Юбки", catalog=catalogs[4]),
            SubCatalog(name="Карнизы", catalog=catalogs[3]),
            SubCatalog(name="Кисти", catalog=catalogs[3]),
            SubCatalog(name="Детская одежда", catalog=catalogs[1]),
            SubCatalog(name="Платки", catalog=catalogs[1]),
            SubCatalog(name="Довяз", catalog=catalogs[7]),
            SubCatalog(name="Крючки", catalog=catalogs[7]),
            SubCatalog(name="Косая", catalog=catalogs[7]),
            SubCatalog(name="шторные", catalog=catalogs[6]),
            SubCatalog(name="Креп", catalog=catalogs[6]),
        ]
        SubCatalog.objects.bulk_create(subCatalogs)
        return subCatalogs
