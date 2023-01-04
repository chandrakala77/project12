from django.urls import path
from app2.views import *
app_name='laddu'

urlpatterns=[
    path('chandhu/',chandhu,name='chandhu'),
]