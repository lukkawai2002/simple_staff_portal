from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_registration.urls')),
    path('portal/', include('portal.urls')),
    path('booking/', include('booking_api.urls')),
    path('product/', include('product_api.urls')),
    path('staff/', include('staff_api.urls')),
]
