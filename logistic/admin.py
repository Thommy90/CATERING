from django.contrib import admin
from .models import DeliveryDishesOrder
from unfold.admin import ModelAdmin

@admin.register(DeliveryDishesOrder)
class DeliveryDishesOrderAdmin(ModelAdmin):
    list_display = ('provider', 'status', 'addresses')
    list_filter = ('provider', 'status')
    search_fields = ('external_order_id',)

    dashboard_charts = [
        {
            'title': 'Deliveries by Status',
            'type': 'pie',
            'labels': lambda self: [status[1] for status in self.model.DELIVERY_STATUSES_CHOICES],
            'data': lambda self: [self.model.objects.filter(status=status[0]).count() for status in self.model.DELIVERY_STATUSES_CHOICES],
        },
        {
            'title': 'Deliveries by Provider',
            'type': 'bar',
            'labels': lambda self: [provider[1] for provider in self.model.PROVIDERS_CHOICES],
            'data': lambda self: [self.model.objects.filter(provider=provider[0]).count() for provider in self.model.PROVIDERS_CHOICES],
        },
        {
            'title': 'Daily Delivery Performance',
            'type': 'line',
            'labels': lambda self: [delivery.created_at.strftime('%Y-%m-%d') for delivery in self.model.objects.order_by('created_at')[:28]],
            'data': lambda self: [self.model.objects.filter(created_at__date=delivery.created_at.date()).count() for delivery in self.model.objects.order_by('created_at')[:28]],
        }
    ]