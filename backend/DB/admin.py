from django.contrib import admin
from .models import *
from .AdminModel.Product.ProductAdmin.admin import ProductAdmin
from .AdminModel.Catalog.AdminCatalog.admin import CatalogAdmin
from .AdminModel.Image.ProductImg.admin import ProductImageAdmin
from .AdminModel.Color.admin import ColorAdmin
from .AdminModel.Size.admin import SizeAdmin
from .AdminModel.Tags.admin import TagsAdmin

# Register your models here.
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Product, ProductAdmin)

# Change the name of the admin site
admin.site.site_title = "Антураж"
admin.site.site_header = "Антураж"
