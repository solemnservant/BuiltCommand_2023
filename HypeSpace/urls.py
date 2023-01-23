"""
Definition of urls for HypeSpace.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import include, url
import Landing_Page.views
admin.autodiscover()


urlpatterns = [
    #url(r'^about$', Landing_Page.views.about, name='about'),
   #url(r'^$', Landing_Page.views.index, name='index'),
    #url(r'^home$', Landing_Page.views.index, name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    path ('users/', include('users.urls')),
    path('members/', include('members.urls')),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    ]
