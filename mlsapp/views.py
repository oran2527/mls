from django.shortcuts import render
from .forms import DataForm

# Create your views here.

def index(request):
    form = DataForm()
    context = {
        'form': form, 
    }
    return render(request, 'mlsapp/index.html', context)

def predictions(request):
    return render(request, 'mlsapp/predictions.html')