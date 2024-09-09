from django.contrib import admin
from .models import Products, Order

# Register your models here.

# admin header name changed
admin.site.site_header = 'E-commerce Site'
admin.site.site_title = 'ABC Shopping'
admin.site.index_title = 'Manage ABC Shpping'

class ProductsAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category='Default')
    change_category_to_default.short_description = 'Change category to Default'


    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ('title','category',)
    actions = ('change_category_to_default',)
    fields = ('title','price',)
    list_editable = ('price','category',)



admin.site.register(Products,ProductsAdmin)
admin.site.register(Order)
