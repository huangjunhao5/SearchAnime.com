"""HTML5Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from . import settings
from django.conf.urls.static import static

import MainPage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Anime/', include('Anime.urls')),
    path('AppUser/', include('AppUser.urls')),
    path('Comment/', include('Comment.urls')),
    path('MainPage/', TemplateView.as_view(template_name="index.html")),
    path('', TemplateView.as_view(template_name="index.html")),
    path('login/', TemplateView.as_view(template_name="login.html")),
    path('register/', TemplateView.as_view(template_name="register.html")),
    path('UserMainPage/', TemplateView.as_view(template_name='UserMainPage.html')),
    path('NotFoundPage/', TemplateView.as_view(template_name='NotFoundPage.html')),
    path('Test/', TemplateView.as_view(template_name='Test.html')),
    path('favicon.ico/', MainPage.views.icon)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
