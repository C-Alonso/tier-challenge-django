from django.contrib import admin
from .models import Address, Counter


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'short')

@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('visits', 'addressId')
