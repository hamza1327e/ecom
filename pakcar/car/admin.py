from django.contrib import admin

# Register your models here.
from car.models import Contact, Product, Category, Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Contact)
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order)
