from django.urls import path
from ultracomp import views

urlpatterns = [
    path('laptop/', views.laptop, name='laptop'),
]