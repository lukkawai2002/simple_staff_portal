from django.urls import path
from .views import Main, Login, Registration

app_name = 'login_registration'

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('login_page', Login.as_view(), name='login_page'),
    path('registration_page', Registration.as_view(), name='registration_page'),
]