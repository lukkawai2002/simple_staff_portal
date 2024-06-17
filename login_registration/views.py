from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from .models import LoginRegistration
import os, hashlib

class Main(View):

    def get(self, request):

        if request.session.get('login'):
            
            return redirect('portal:portal')
        else:

            return render(request, 'main.html')
        
class Login(View):

    def get(self, request):

        if request.session.get('login'):
            
            return redirect('portal:portal')
        else:

            return render(request, 'login_page.html')
        
            
    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:

            login = LoginRegistration.objects.get(username = username)

        except LoginRegistration.DoesNotExist:

            login_fail_message = 'Username or password incorrect.'
            alert_style = 'alert alert-danger'
     
            messages.error(request, login_fail_message, extra_tags=alert_style)

            return redirect('login_registration:login_page')
        
        stored_salt = login.salt
        stored_hashed_password = login.password

        password_bytes = password.encode('utf-8')
        hashed_input_password = hashlib.sha256(password_bytes + stored_salt).hexdigest()
        print(hashed_input_password)

        if hashed_input_password == stored_hashed_password:

            request.session['login'] = True

            return redirect('portal:portal')
        
        else:

            return redirect('login_registration:login_page')
    
class Registration(View):

    def get(self, request):

        return render(request, 'registration_page.html')
    
    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')


        if LoginRegistration.objects.filter(username = username).exists():

            username_used_message = 'Username had been used.'
            messages.error(request, username_used_message)

            return redirect('login_registration:registration_page')
        else:
            
            salt = os.urandom(16)
            password_bytes = password.encode('utf-8')
            hashed_password = hashlib.sha256(password_bytes + salt).hexdigest()

            registration = LoginRegistration(username = username, password = hashed_password, salt = salt)
            registration.save()
            print(hashed_password)

            registration_success_message = 'Registration is succcessful.'
            success_style = 'alert alert-success'

            messages.success(request, registration_success_message, extra_tags=success_style)
        
            return redirect('login_registration:login_page')