from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.homepage ,name='homepage'),
    path('about/',views.about ,name='about'),
    path('service/',views.service ,name='service'),
    path('contact/',views.contact ,name='contact'),
]
