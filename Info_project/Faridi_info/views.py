from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import InformationForm
from .models import Information
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import RegisterForm


# Create your views here.

#Register Page
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') # Access the cleaned (validated) username
            password = form.cleaned_data.get('password') # Access the cleaned (validated) password
            user = User.objects.create_user(username=username, password=password)
            # No need to call user.save() because `create_user()` already does this internally.
           
            return redirect('login')
    else:
        form = RegisterForm()  # Initialize the form for GET request
    
    return render(request, 'accounts/register.html', {'form': form})

#Login Page
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'my_view'
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')  # Optional: To show an error message
            return render(request, 'accounts/login.html')

    # If GET request (initial page load), just render the login page
    return render(request, 'accounts/login.html')
        

#Logout Page
def logout_view(request):
    if request.method == 'POST':
        logout(request) 
        return redirect('login')   
    else:
        return redirect('my_view')   
    
 
# Home Page
# Using decorator
@login_required
def home_view(request):
    return render(request, 'information/home.html')


# Protected View, Here anyone who does not register or login can not access this page
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'information/protected.html')


# CREATE INFO PAGE
@login_required
def create_page_view(request):
    
    if request.method == 'POST':
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save(commit=False) # Don't save to database yet
            user_info.user = request.user  # Attach the logged-in user
            user_info.save() 
            return redirect('info_page')
    else:
        form = InformationForm()
    return render(request, 'information/create_page.html', {"form":form})


# READ INFO PAGE
@login_required
def success_page_view(request):
    my_info = Information.objects.filter(user=request.user)
    return render(request, 'information/success_page.html', {"my_info":my_info} )


# UPDATE INFO PAGE
def update_info_page(request, id):
    my_info = Information.objects.get(id=id)
    if request.method == 'POST':
        form = InformationForm(request.POST, request.FILES, instance=my_info)
        if form.is_valid():
            form.save()
            return redirect('info_page')
    else:
         form = InformationForm(instance=my_info)
    return render(request, 'information/create_page.html', {"form":form})
    

#DELETE PAGE
def delete_info_page(request, id):
    my_info = Information.objects.get(id=id)
    if request.method == 'POST':
        my_info.delete()
        return redirect('info_page')
        
    return render(request, 'information/delete_confirm.html', {"my_info":my_info})


