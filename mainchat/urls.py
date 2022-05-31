from django.urls import path
from .views import *

urlpatterns = [
    path('', chat, name='home'),
    path('add/', receive, name='add'),
    path('check/', check, name='check')
]
