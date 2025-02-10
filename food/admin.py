from django.contrib import admin
from .models import Restaurant, Dish, DishesOrder, DishOrderItem
from unfold.admin import ModelAdmin
from django.db.models import Sum

@admin.register(Restaurant)
class RestaurantAdmin(ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)


@admin.register(Dish)
class DishAdmin(ModelAdmin):
    list_display = ('name', 'price', 'restaurant')
    list_filter = ('restaurant',)
    search_fields = ('name',)

    def changelist_view(self, request, extra_context=None):
        order_counts = (
            DishOrderItem.objects
            .values('dish__name')
            .annotate(total=Sum('quantity'))
            .order_by('-total')
            .distinct()[:20]
        )

        labels = [item['dish__name'] for item in order_counts]
        data = [item['total'] for item in order_counts]

        print("Labels:", labels)
        print("Data:", data)

        extra_context = extra_context or {}
        extra_context['chart_data'] = {
            'labels': labels,
            'data': data,
        }
        return super().changelist_view(request, extra_context=extra_context)



@admin.register(DishesOrder)
class DishesOrderAdmin(ModelAdmin):
    list_display = ('external_order_id', 'user', 'created_at')
    search_fields = ('external_order_id',)


@admin.register(DishOrderItem)
class DishOrderItemAdmin(ModelAdmin):
    list_display = ('order', 'dish', 'quantity')