from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Successful login
            login(request, user)
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))
        else:
            # undefined user or wrong password
            context = {
                'username': username,
                'error': 'کاربری با این مشخصات یافت نشد'
            }
    else:
        context = {}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))