from django.urls import path, include
from rest_framework import routers
from . import views  # Import views from listings app

router = routers.DefaultRouter()
router.register(r'listings', views.ListingViewSet, basename='listing')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]
