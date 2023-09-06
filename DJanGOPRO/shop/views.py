from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello world")

def go(request):
    return HttpResponse("GoGoGo!")

def domashka(request):
    return HttpResponse("Domashka Vypolnena?")