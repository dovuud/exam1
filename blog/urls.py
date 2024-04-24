from django.urls import path
from .views import home_page

urlpattern = [
    path('',home_page,name='home_page')
]