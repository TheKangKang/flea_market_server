from django.shortcuts import render


def user_login(request):
    return render(request, 'user/user_login.html')


def user_reg(request):
    return render(request, 'user/user_reg.html')
