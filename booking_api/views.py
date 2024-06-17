from django.shortcuts import redirect
from .serializer import BookingSerializer
from .models import Booking
from rest_framework import generics

class BookingListCreate(generics.ListCreateAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
        
    def get(self, request, *args, **kwargs):

        if request.session.get('login'):

            return super().get(request, *args, **kwargs)
        else:

            return redirect('login_registration:main')
            
class BookingSearch(generics.RetrieveAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get(self, request, *args, **kwargs):

        if request.session.get('login'):

            return super().get(request, *args, **kwargs)
        else:

            return redirect('login_registration:main')
