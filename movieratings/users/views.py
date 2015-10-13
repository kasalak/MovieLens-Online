from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserForm
from .models import UserProfile

# Create your views here.


def login(request):
    if request.method == 'POST':
        # attempting to login
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=user.username,
                            password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "Ready to rate, {}?".format(user.username))
            return redirect('top_movies')

        else:
            return render(request,
                          'users/login.html',
                          {'failed': True,
                           'username': username})

    return render(request,
                  'users/login.html',
                  )
def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password

            user.set_password(password)
            user.save()

            profile = UserProfile(
                user=user,
            )
            profile.save()

            user = authenticate(username=user.username, password=password)

            login(request, user)
            return redirect('top_movies')
    else:
        form = UserForm()
    return render(request, 'users/register.html',
                 {'form': form})


def logout_view(request):
    logout(request)
    return redirect('top_movies')
