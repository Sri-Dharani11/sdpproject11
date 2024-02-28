# from django.contrib import admin
# from django.urls import path
#
# from.views import *
#
# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('hello/',hello1,name='hello'),
#     path('newHomePage/', newHomePage, name='newHomePage'),
#     path('travelPackage/',travelPackage,name='travelPackage')
#
# ]

from django.contrib import admin
from django.urls import path, include
from.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello1/', hello1, name='hello1'),
    path('',newHomePage, name='newHomePage'),
    path('travelPackage/', travelPackage, name='travelPackage'),
    path('print1/', print_to_console, name='print_to_console'),
    path('p/', print1, name='print1'),
    path('print3/', generate_otp, name='generate_otp'),
    path('p1/', print2, name='print2'),
    path('print4/',get_date, name='get_date'),
    path('p2/', getdate1, name='getdate1'),
    path('print5/',registerloginfunction, name='registerloginfunction'),
    path('p3/', getregistercall, name='getregistercall'),
    path('print6/', pie_chart, name='pie_chart'),
    path('p4/', piechartcall, name='piechartcall'),
    path('p5/', rent_car, name='rent_car'),
    path('weathercall/',weatherpagecall,name='weatherpagecall'),
    path('weather/',weatherlogic,name='weatherlogic'),
    path('feedbackformcall/',feedbackformcall,name='feedbackformcall'),
    path('feedbackformfunction/',feedbackformfunction,name='feedbackformfunction'),
    path('login/', login, name='login'),
    path('register/',signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('login1/', login1, name='login1'),
    path('signup1/', signup1, name='signup1'),

]

