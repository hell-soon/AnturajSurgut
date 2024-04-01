from django import forms
from ...widgets.Preview.ProductPreview import ImageWidget
from DB.models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "image": ImageWidget,
        }
