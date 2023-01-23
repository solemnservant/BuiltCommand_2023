"""Defines URL patterns for members."""

from django.urls import path
from django.conf.urls import url

from .import views

app_name = 'members'
urlpatterns = [
    #Company Page
    path('index/', views.index, name = 'index'),
    
    #Page for listing all members
    path('all_members/', views.all_members, name = 'all_members'),

    #Page for adding a new Member
    path('member/<int:member_id>/', views.member, name = 'member'),

    #Page for adding a new Member office using a form
    path('new_member/', views.new_member, name = 'new_member'),

    #Page for a company to edit their entry.
    path('edit_member/<int:member_id>/', views.edit_member, name = 'edit_member'),
    ] 