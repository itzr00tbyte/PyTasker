from django.urls import path
from . import views
"""from django.contrib.auth import as auth_views"""
urlpatterns = [
    path('',views.home,name='home'),
    path('Currency',views.currency,name='Currency'),
]