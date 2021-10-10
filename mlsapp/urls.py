from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='mslapp-index'),
    path('predictions/', views.predictions, name='mlsapp-predictions')
]