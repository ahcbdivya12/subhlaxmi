"""
URL configuration for tms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

from web_tms import views as web_tms_views
from web_tms import views as web_tms_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('service.urls')),


    # path('admin/', .site.urls),
    
    path('',web_tms_views.index ),
    path('contact',web_tms_views.contact),
    path('about',web_tms_views.about),
    path('agent',web_tms_views.agent),
    path('list',web_tms_views.list),
    path('agent',web_tms_views.agent),
    path('Inquiry',web_tms_views.Inquiry),
    path('type',web_tms_views.type),
        path('book',web_tms_views.book),
        path('sigin',web_tms_views.sigin),
        path('sigup',web_tms_views.sigup),
        path('logout',web_tms_views.LogoutPage),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

