from django import forms
from django.utils.safestring import mark_safe
from DB.models import ProductImage


class ImageWidget(forms.SelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value:
            images = ProductImage.objects.filter(id__in=value)
            html += '<div class="image-preview">'
            for image in images:
                html += f'<a href="{image.image.url}"><img class="block-image" src="{image.image.url}" alt="{image.image.name}"></a>'
            html += "</div>"
        return mark_safe(html)


# background-color: white; border: 1px solid #aaa; border-radius: 4px; cursor: text; padding-bottom: 5px; padding-right: 5px; position: relative;
