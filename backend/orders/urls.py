from django.urls import path
from .views import OrderListCreateView, WaypointCreateView

urlpatterns = [
	path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('waypoints/', WaypointCreateView.as_view(), name='waypoint-create'),
]
