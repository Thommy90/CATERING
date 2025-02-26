from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status, viewsets, routers
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Dish, DishOrderItem, Order, Restaurant
from .serializers import DishSerializer, OrderSerializer, RestaurantSerializer
from food.enums import OrderStatus


class FoodAPIViewSet(viewsets.GenericViewSet):
    # GET /food/restaurants
    @action(methods=["get"], detail=False,)
    def restaurants(self, request):
        restaurants = Restaurant.objects.all()
        if not restaurants.exists():
            return Response({"error": "No restaurants found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(data=serializer.data)

    # POST /food/restaurants
    @action(methods=["post"], detail=False, url_path="restaurants/create")
    def create_restaurant(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if not request.data.get('name'):
            return Response({"error": "Restaurant name is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not request.data.get('address'):
            return Response({"error": "Restaurant address is required"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # GET /food/restaurants/{restaurant_id}/
    @action(methods=["get"], detail=False, url_path="restaurants/(?P<restaurant_id>[^/.]+)")
    def retrieve_restaurant(self, request, restaurant_id=None):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    # HTTP GET /food/dishes
    @action(methods=["get"], detail=False)
    def dishes(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)

        return Response(data=serializer.data)

    # HTTP POST /food/orders
    @action(methods=["post"], detail=False)
    def orders(self, request: WSGIRequest):
        """create new order for food.

        HTTP REQUEST EXAMPLE
        {
            "food": {
                1: 3  // id: quantity
                2: 1  // id: quantity
            }
        }


        WORKFLOW
        1. validate the input
        2. create ``
        """

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not isinstance(serializer.validated_data, dict):
            raise ValueError(...)

        # alternatives
        # -------------
        # assert isinstance(serializer.validated_data, dict)

        # from typing import cast
        # response = cast(dict, serializer.validated_data) | {}

        # ACTIVE RECORD
        # =======================
        # order = Order(status=OrderStatus.NOT_STARTED, provider=None)
        # order.save()

        # ORM
        # ======================
        order = Order.objects.create(status=OrderStatus.NOT_STARTED, user=request.user)
        print(f"New Food Order is created: {order.pk}")

        try:
            dishes_order = serializer.validated_data["food"]
        except KeyError as error:
            raise ValueError("Food order is not properly built")

        for dish_order in dishes_order:
            instance = DishOrderItem.objects.create(
                dish=dish_order["dish"], quantity=dish_order["quantity"], order=order
            )
            print(f"New Dish Order Item is created: {instance.pk}")

        return Response(
            data={},
            status=status.HTTP_201_CREATED,
        )




router = routers.DefaultRouter()
router.register(
    prefix="food",
    viewset=FoodAPIViewSet,
    basename="food",
)