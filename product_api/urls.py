from django.urls import path
from .views import ProductListCreate, ProductSearch

app_name = 'product_api'

urlpatterns = [
    path('product_list_create', ProductListCreate.as_view(), name='product_list_create'),
    path('product_search/<int:pk>', ProductSearch.as_view(), name='product_search'),
]
