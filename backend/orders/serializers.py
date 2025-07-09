from rest_framework import serializers
from .models import Order, Waypoint

class WaypointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Waypoint
		fields = ['id', 'order', 'location', 'waypoint_type']

class OrderSerializer(serializers.ModelSerializer):
	waypoints = WaypointSerializer(many=True, read_only=True)

	class Meta:
		model = Order
		fields = ['id', 'order_number', 'customer_name', 'date', 'waypoints']