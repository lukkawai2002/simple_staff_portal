from django.urls import path
from .views import BookingListCreate, BookingSearch
app_name = 'booking_api'

urlpatterns = [
    path('booking_list_create', BookingListCreate.as_view(), name='booking_list_create'),
    path('booking_search/<int:pk>', BookingSearch.as_view(), name='booking_search'),
]
