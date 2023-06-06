from django.urls import path
from ultracomp import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('details/<int:id>/', views.details,name="details"),
    path('delete/<int:id>/' ,views.deleteComment,name="delete_comment")
]