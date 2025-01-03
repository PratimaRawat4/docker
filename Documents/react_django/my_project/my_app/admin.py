from django.contrib import admin
from .models import Product
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'area', 'year', 'category', 'image_preview','rating')  # Added 'category' and 'image_preview'
    list_filter = ('brand', 'area', 'year', 'category','rating')  # Updated list_filter to include 'category'
    search_fields = ('name', 'description', 'brand', 'area', 'category')  # Updated search_fields to include 'category'
    ordering = ('year', 'name')  # Keeps the same ordering
    readonly_fields = ('image_preview',)  # Optional: Display image preview in the admin detail view

    # Custom method to preview image in the admin interface
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.image.url)
        return "No image available"
    image_preview.short_description = 'Image Preview'

    # Optional: Add more user-friendly configurations
    list_per_page = 20  # Limits the number of products displayed per page
    save_on_top = True  # Places Save/Save and Continue buttons at the top of the admin page

