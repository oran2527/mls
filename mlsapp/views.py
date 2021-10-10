from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mlsapp/index.html')

def predictions(request):
    return render(request, 'mlsapp/predictions.html')