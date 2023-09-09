from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def go(request):
    return HttpResponse("GoGoGo!")

def domashka(request):
    return HttpResponse("Domashka Vypolnena?")

def shop(request):
    return render(request, 'shop/shop.html')