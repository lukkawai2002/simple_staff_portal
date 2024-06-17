from django.shortcuts import redirect
from .models import Staff
from .serializer import StaffSerializer
from rest_framework import generics

class StaffListCreate(generics.ListCreateAPIView):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get(self, request, *args, **kwargs):

        if request.session.get('login'):

            return super().get(request, *args, **kwargs)
        else:

            return redirect('login_registration:main')

class StaffSearch(generics.RetrieveAPIView):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get(self, request, *args, **kwargs):

        if request.session.get('login'):

            return super().get(request, *args, **kwargs)
        else:

            return redirect('login_registration:main')