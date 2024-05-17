from django.urls import path
from .views import HomePageView,AboutPageView,ServicesPageView,ContactPageView,AppointmentPageView

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('services/', ServicesPageView.as_view(),name='services'),
    path('contact/', ContactPageView.as_view(),name='contact'),
    path('appointment/', AppointmentPageView.as_view(),name='appointment'),
]