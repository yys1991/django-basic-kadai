from django.contrib import admin
from .models import Product,Category
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category','image','description')
    search_fields = ('name',)
    list_filter = ('category',)

    def image(self, obj):
        if obj.img:
            return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.img.url))
        return "No image"

    image.short_description = 'Image'
     

class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name")
    search_fields=("name",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)