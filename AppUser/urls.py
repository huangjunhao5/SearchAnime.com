from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = {
    path('api/login/', views.signin),
    path('api/register/', views.Register),
    path('api/logout/', views.Logout),
    path('api/GetUserInformation/<str:uid>', views.GetUserInformation),
    path('api/GetNowUser/', views.NowUser),
    path('api/ChangeUserInfo/<str:uid>', views.ChangeUserInfo),
    path('api/ChangeUserPassword/<str:uid>', views.ChangeUserPassword),
    path('api/GetVisited/<str:uid>', views.GetVisited),
}
