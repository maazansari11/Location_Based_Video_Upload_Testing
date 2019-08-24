"""directory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from myapp import views as users_views, views
app_name = 'myapp'


urlpatterns = [

    path('admin/', admin.site.urls),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login_form.html'), name='login'),
    path('upload/',views.upload, name='upload'),
    path('poc/<domain_type>', views.load_countries, name='poc'),
    path('video_type/', views.video_type, name='video_type'),
    path('video_type/<online_offline_video>', views.video_type_details, name='video_type_details'),
    path('video_type/<online_offline_video>/domain_type', views.domain_type, name='domain_type'),
    path('video_type/<online_offline_video>/domain_type/<domain_type>', views.domain_type_details, name='domain_type_details'),
    path('video_type/<online_offline_video>/domain_type/<domain_type>/location', views.location, name='location'),
    path('video_type/<online_offline_video>/domain_type/<domain_type>/location/<country>', views.location, name='location_country'),
    path('load_states/<domain_type_id>/<country_id>', views.load_states, name='load_states'),
    path('load_cities/<state_id>', views.load_cities, name='load_cities'),

]
