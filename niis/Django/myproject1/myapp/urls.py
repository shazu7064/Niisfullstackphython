from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #basic pages
    path('',views.home),
    path('about/',views.about),

    
    path('home1/',views.contact),
    path('about1/',views.contact),
    path('contact/',views.contact),
    path('services/',views.services),

    #dynamic URL
    path('welcome/<str:name>/',views.welcome),
]
