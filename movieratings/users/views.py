from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserForm, RaterForm
from thumbsup.models import Rater

# Create your views here.


def user_login(request):
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
        user_form = UserForm(request.POST)
        rater_form = RaterForm(request.POST)
        if user_form.is_valid() and rater_form.is_valid():
            user = user_form.save()
            password = user.password

            rater = rater_form.save(commit=False)
            rater.user = user
            rater.save()

            user.set_password(password)
            user.save()

            user = authenticate(username=user.username, password=password)

            login(request, user)
            return redirect('top_movies')
    else:
        user_form = UserForm()
        rater_form = RaterForm()
    return render(request, 'users/register.html',
                  {'user_form': user_form,
                   'rater_form': rater_form})


def user_logout(request):
    logout(request)
    return redirect('top_movies')
