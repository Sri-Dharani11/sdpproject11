
from django.urls import path, include

from . import views
urlpatterns=[
    path('',views.send_emails,name='send_emails'),
]