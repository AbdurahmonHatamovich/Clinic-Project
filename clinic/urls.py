from django.urls import path, include
from .views import ( AboutPageView, ServicesPageView, ContactPageView, AppointmentPageView,DoctorListView,DoctorDetailView,DoctorCreateView,DoctorUpdateView,DoctorDeleteView)




urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:id>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('update/<int:id>/', DoctorUpdateView.as_view(), name='doctor-update'),
    path('delete/<int:id>/', DoctorDeleteView.as_view(), name='doctor-delete'),
    path('doctor_add/', DoctorCreateView.as_view(), name='doctor-add'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('appointment/', AppointmentPageView.as_view(), name='appointment'),
]
