from django.contrib import admin
from .models import *


@admin.register(DiscountCart)
class DiscountCartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DiscountCart._meta.fields]

    class Meta:
        model = DiscountCart

