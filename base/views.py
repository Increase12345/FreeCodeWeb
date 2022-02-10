from django.shortcuts import render

def index(request):
    return render(request, 'base/index.html')

def cart(request):
    return render(request, 'base/cart.html')

def guitar(request):
    return render(request, 'base/guitar.html')
