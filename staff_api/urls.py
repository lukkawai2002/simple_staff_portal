from django.urls import path
from .views import StaffListCreate, StaffSearch

app_name = 'staff_api'

urlpatterns = [
    path('staff_list_create', StaffListCreate.as_view(), name='staff_list_create'),
    path('staff_search/<int:pk>', StaffSearch.as_view(), name='staff_search'),
]
