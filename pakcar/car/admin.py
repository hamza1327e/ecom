from django.contrib import admin
from car.models import Contact, Product, Category, Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category','created_at','updated_at']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Contact)
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order)