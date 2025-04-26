from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'property_type', 'transaction_type', 'city', 'created_at')
    list_filter = ('property_type', 'transaction_type', 'city')
    search_fields = ('title', 'description', 'address', 'city')
    date_hierarchy = 'created_at'
