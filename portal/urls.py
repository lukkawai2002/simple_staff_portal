from django.urls import path
from .views import Portal, StaffInformation, StaffUpdate, StaffDelete, ProductDetail, ProductUpdate, ProductDelete, BookingRecord, BookingUpdate, BookingDelete, Logout

app_name = 'portal'

urlpatterns = [
    path('', Portal.as_view(), name='portal'),
    path('staff_information', StaffInformation.as_view(), name='staff_information'),
    path('staff_update', StaffUpdate.as_view(), name='staff_update'),
    path('staff_delete', StaffDelete.as_view(), name='staff_delete'),
    path('product_detail', ProductDetail.as_view(), name='product_detail'),
    path('product_update', ProductUpdate.as_view(), name='product_update'),
    path('product_delete', ProductDelete.as_view(), name='product_delete'),
    path('booking_record', BookingRecord.as_view(), name='booking_record'),
    path('booking_update', BookingUpdate.as_view(), name='booking_update'),
    path('booking_delete', BookingDelete.as_view(), name='booking_delete'),
    path('logout', Logout.as_view(), name='logout'),
]