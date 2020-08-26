from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.forms import SignupForm, LoginForm
from homepage.models import MyUser
from django.contrib.auth import login, authenticate
from custom_user.settings import AUTH_USER_MODEL


# Create your views here.

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create(
                username = data.get('username'),
                displayname = data.get('displayname'),
                password = data.get('password')
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))


    return render(request, 'generic_form.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, 
                username=data.get('username'), 
                password=data.get('password')
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))


    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def homepage_view(request):

    return render(request, 'homepage.html', {'model_check': AUTH_USER_MODEL})