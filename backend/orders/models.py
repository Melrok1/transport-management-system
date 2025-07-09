from django.db import models

class Order(models.Model):
	order_number = models.CharField(max_length=100)
	customer_name = models.CharField(max_length=100)
	date = models.DateField()

	def __str__(self):
		return f'{self.order_number} - {self.customer_name}'

class Waypoint(models.Model):
	PICKUP = 'pickup'
	DELIVERY = 'delivery'

	WAYPOINT_TYPES = [
		(PICKUP, 'Pickup'),
		(DELIVERY, 'Delivery'),
	]

	order = models.ForeignKey(Order, related_name='waypoints', on_delete=models.CASCADE)
	location = models.CharField(max_length=200)
	waypoint_type = models.CharField(max_length=10, choices=WAYPOINT_TYPES)

	def __str__(self):
		return f'{self.location} ({self.waypoint_type})'