from django.shortcuts import render

from rest_framework import generics, filters
from .models import Order, Waypoint
from .serializers import OrderSerializer, WaypointSerializer

class OrderListCreateView(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class WaypointCreateView(generics.CreateAPIView):
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer
    
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer_name', 'date']
