"""uasys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from pages.views import login_view, profile_view, home_view, new_event_view, new_action_view, enrollment_view
from user.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/', profile_view, name='profile'),
    path('register/', register, name='register'),
    path('home/', home_view, name='home'),
    path('home/', new_event_view, name='event_refresh'),
    path('home2/', new_action_view, name='action_refresh'),
    path('enroll/', enrollment_view, name='enroll'),
]
