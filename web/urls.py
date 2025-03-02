"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path ,include
from web import views
from django.conf import settings
from django.conf.urls.static import static
from info.views import *
# from profileapp.views import profile
# Enabling static files serving
# Including the profileapp urls

urlpatterns = [
    path('/', include('profileapp.urls')),
    path('info/', include('info.urls')), 
    path('contact/', contact_view, name='contact'), 
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about),
    path('about/<int:courseid>', views.detail),
    path('services/', views.services, name='services'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('submitform/', views.submit, name='submitform'),
    path('marks/', views.marks, name='marks'),
    path('logout/', views.logout, name='logout'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
