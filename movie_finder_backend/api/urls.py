from django.urls import path
from api import views


urlpatterns = [
    path('test/', views.test),
    path('genres/', views.genres),
    path('genres/<int:id>/movies/', views.movie_by_genre),
    
]