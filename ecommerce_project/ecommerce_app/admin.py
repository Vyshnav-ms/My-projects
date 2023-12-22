from django.contrib import admin

# Register your models here.
from . models import Category,Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','slug']
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    list_per_page = 20
    prepopulated_fields ={'slug':('product_name',)}
admin.site.register(Product,ProductAdmin)