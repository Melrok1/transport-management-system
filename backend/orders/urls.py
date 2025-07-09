from django.urls import path
from .views import OrderListCreateView, OrderDetailView, WaypointCreateView

urlpatterns = [
	path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('waypoints/', WaypointCreateView.as_view(), name='waypoint-create'),
]
