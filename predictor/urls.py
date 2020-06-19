from django.urls import path
from predictor import views

urlpatterns = [
    
    path('', views.home, name='home'),
   
    
   
]