from django.shortcuts import render

from rest_framework import generics
from .models import Order, Waypoint
from .serializers import OrderSerializer, WaypointSerializer

class OrderListCreateView(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class WaypointCreateView(generics.CreateAPIView):
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer
