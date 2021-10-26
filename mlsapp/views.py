from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mlsapp-predictions')
    else:
        form = DataForm()
    context = {
        'form': form, 
    }
    return render(request, 'mlsapp/index.html', context)

def predictions(request):
    predicted_sports = Data.objects.all()
    context = {
        'predicted_sports': predicted_sports  
    }
    return render(request, 'mlsapp/predictions.html', context)