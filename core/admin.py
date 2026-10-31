
from django.contrib import admin
from .models import WebsiteProduct, WebsiteOrder


@admin.register(WebsiteProduct)
class WebsiteProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(WebsiteOrder)
class WebsiteOrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'email',
        'phone',
        'message',
        'website',
        'payment_method',
        'status',
        'created_at',
    )
    list_editable = ('status',)
    list_filter = ('status', 'payment_method')
    search_fields = ('customer_name', 'email', 'phone')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
   
