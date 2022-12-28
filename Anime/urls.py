from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = {
    path('api/SetAnimeDatabase', views.SetAnimeDatabase),
    path('api/GetAnimeByMediaId/<int:mid>', views.GetAnimeByMediaId),
    path('api/GetAllAnime', views.GetAllAnime),
    path('api/SearchAnime/<str:keyword>', views.SearchAnime),
    path('api/SetAnimeTag/', views.SetAnimeTag),
    path('api/GetAnimeByTag/<str:TagName>', views.GetAnimeByTag),
    path('api/GetAllAnimeTitle/', views.GetAllAnimeTitle),
    path('api/GetUnFinishedAnime/', views.GetUnFinishedAnime),
    path('api/GetMostHotAnime/', views.GetMostHotAnime),
}