from django.shortcuts import redirect
from .serializer import ProductSerializer
from .models import Product
from rest_framework import generics

class ProductListCreate(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):

        if request.session.get('login'):

            return super().get(request, *args, **kwargs)
        else:

            return redirect('login_registration:main')
    
class ProductSearch(generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):

        if request.session.get('login'):

            return super().get(request, *args, **kwargs)
        else:

            return redirect('login_registration:main')
