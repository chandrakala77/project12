from django.urls import path
from app1.views import *
app_name='bunny'

urlpatterns=[
    path('allu/',allu,name='allu'),
]