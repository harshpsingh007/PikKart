from django.contrib import admin
from .models import Cars

# Register your models here.
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ("Brand","model_name","active","created","updated")
    list_filter = ("Brand","created","model_name")
    search_fields = ("Brand","model_name")