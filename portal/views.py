from django.views import View
from django.shortcuts import redirect, render
from staff_api.models import Staff
from product_api.models import Product
from booking_api.models import Booking

class Portal(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'portal.html')
        else:

            return redirect('login_registration:main')

class StaffInformation(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'staff_information.html')
        else:

            return redirect('login_registration:main')

class StaffUpdate(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'staff_update.html')
        else:

            return redirect('login_registration:main')

    def post(self, request):

        id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        position = request.POST.get('position')
        department = request.POST.get('department')
        salary = request.POST.get('salary')

        try:

            update_staff = Staff.objects.get(pk=id)
        except Staff.DoesNotExist:

            return redirect('staff_api:staff_search', pk=id)
        
        update_staff.name = name
        update_staff.age = age
        update_staff.gender = gender
        update_staff.position = position
        update_staff.department = department
        update_staff.salary = salary
        update_staff.save()

        return redirect('staff_api:staff_list_create')

class StaffDelete(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'staff_delete.html')
        else:

            return redirect('login_registration:main')

    def post(self, request):

        id = request.POST.get('id')

        try:

            staff = Staff.objects.get(pk=id)
        except Staff.DoesNotExist:

            return redirect('staff_api:staff_search', pk=id)
        
        staff.delete()

        return redirect('staff_api:staff_list_create')

class ProductUpdate(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'product_update.html')
        else:

            return redirect('login_registration:main')

    def post(self, request):

        id = request.POST.get('id')
        product = request.POST.get('product')
        category = request.POST.get('category')
        inventory = request.POST.get('inventory')
        price = request.POST.get('price')

        try:

            update_product = Product.objects.get(pk=id)
        except Product.DoesNotExist:

            return redirect('product_api:product_search', pk=id)
        
        update_product.product = product
        update_product.category = category
        update_product.inventory = inventory
        update_product.price = price
        update_product.save()

        return redirect('product_api:product_list_create')

class ProductDelete(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'product_delete.html')
        else:

            return redirect('login_registration:main')

    def post(self, request):

        id = request.POST.get('id')

        try:

            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:

            return redirect('product_api:product_search', pk=id)
        
        product.delete()

        return redirect('product_api:product_list_create')
    
class ProductDetail(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'product_detail.html')
        else:

            return redirect('login_registration:main')
    
class BookingRecord(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'booking_record.html')
        else:

            return redirect('login_registration:main')

class BookingUpdate(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'booking_update.html')
        else:

            return redirect('login_registration:main')

    def post(self, request):

        id = request.POST.get('id')
        customer = request.POST.get('customer')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        booking_status = request.POST.get('booking_status')
        payment_status = request.POST.get('payment_status')
        payment_method = request.POST.get('payment_method')
        payment_date = request.POST.get('payment_date')
        payment_amount = request.POST.get('payment_amount')
        service = request.POST.get('service')

        try:

            update_booking = Booking.objects.get(pk=id)
        except Booking.DoesNotExist:

            return redirect('booking_api:booking_search', pk=id)
        
        update_booking.customer = customer
        update_booking.age = age
        update_booking.gender = gender
        update_booking.email = email
        update_booking.phone_number = phone_number
        update_booking.address = address
        update_booking.booking_date = booking_date
        update_booking.booking_time = booking_time
        update_booking.booking_status = booking_status
        update_booking.payment_status = payment_status
        update_booking.payment_method = payment_method
        update_booking.payment_date = payment_date
        update_booking.payment_amount = payment_amount
        update_booking.service = service
        update_booking.save()

        return redirect('booking_api:booking_list_create')

class BookingDelete(View):

    def get(self, request):

        if request.session.get('login'):

            return render(request, 'booking_delete.html')
        else:

            return redirect('login_registration:main')

    def post(self, request):

        id = request.POST.get('id')

        try:

            booking = Booking.objects.get(pk=id)
        except Booking.DoesNotExist:

            return redirect('booking_api:booking_search', pk=id)
        
        booking.delete()

        return redirect('booking_api:booking_list_create')
    
class Logout(View):

    def get(self, request):

        request.session.flush()
        
        return redirect('login_registration:main')