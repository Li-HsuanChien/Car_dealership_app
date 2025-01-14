# djangoapp/admin.py
from django.contrib import admin
from .models import CarMake, CarModel, CarDealer, DealerReview

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2  # Number of empty forms to display for adding related CarModel objects

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'name', 'car_type', 'year', 'dealer_id')  # Customize the fields displayed in the admin list view



admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
