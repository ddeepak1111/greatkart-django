from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_dispaly       = ('product_name','slug','price','category','is_available','modified_date')
    list_dispaly_links = ( 'product_name','slug')
    prepopulated_fields  = { 'slug':('product_name',)}

admin.site.register(Product,ProductAdmin)