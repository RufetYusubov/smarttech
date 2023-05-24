from django.urls import path
from ultracomp import views

urlpatterns = [
    path('laptop/', views.laptop, name='laptop'),
    path('details/<int:id>/', views.details,name="details")
]