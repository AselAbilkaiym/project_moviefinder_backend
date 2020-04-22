from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('test/', views.test),
    path('genres/', views.genres),
    path('genres/<int:id>/movies/', views.movie_by_genre),
    path('login/', obtain_jwt_token),
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:id>/', views.MovieDetailed.as_view()),
    path('manager/', views.ManagerView.as_view())
]