from django.contrib import admin
from .models import DeliveryDishesOrder
from unfold.admin import ModelAdmin

@admin.register(DeliveryDishesOrder)
class DeliveryDishesOrderAdmin(ModelAdmin):
    list_display = ('provider', 'status', 'addresses')
    list_filter = ('provider', 'status')
    search_fields = ('external_order_id',)
