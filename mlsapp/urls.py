from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='mlsapp-index'),
    path('predictions/', views.predictions, name='mlsapp-predictions')
]