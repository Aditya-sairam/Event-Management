"""stackhack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from event import views as event_views
from django.contrib.auth import views as auth_views
#from django.views.static import serve
#from django.conf.urls.static import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',event_views.EventSearchList.as_view(),name='event-list'),
    path('create',event_views.EventCreateView.as_view(),name='create'),
    path('event-detail/<int:pk>',event_views.EventDetailView.as_view(),name='event-detail'),
    path('event-update/<int:pk>',event_views.EventUpdateView.as_view(),name='event-update'),
    path('event-delete/<int:pk>',event_views.EventDeleteView.as_view(),name='event-delete'),
    path('api/chart/data/',event_views.ChartData.as_view(),name='chart'),
    path('chart',event_views.chart,name='chart-view'),
    path('home/<int:event_id>',event_views.HomeView,name='home-view'),

    path('login/', auth_views.LoginView.as_view(template_name='event/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='event/logout.html'), name='logout'),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
