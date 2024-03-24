from django.shortcuts import render


def index(request):
    return render(request, 'market/index.html')


def productlist(request):
    return render(request, 'market/productlist.html')
