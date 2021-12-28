from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Collection)

@admin.register(models.Product)
class ProductView(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    '''
    def collection_title(self, product):
        return product.collection.title
    '''

    @admin.display(ordering = 'inventory')
    def inventory_status(self, product):
        if(product.inventory < 10):
            return "Low"
        elif(10 <= product.inventory <= 20):
            return "Medium"
        else:
            return "High"

@admin.register(models.Customer)
class CustomerView(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10

@admin.register(models.Order)
class OrderView(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    list_select_related = ['customer']
    list_per_page = 10
