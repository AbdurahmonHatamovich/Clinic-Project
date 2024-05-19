from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .models import Appointment,Contact,Service,Doctor,Comments
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DoctorSerializer,AppointmentSerializer,ContactSerializer,CommentsSerializer,ServiceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status, permissions
from rest_framework.pagination import LimitOffsetPagination
from .forms import DoctorForm
from django.contrib.auth.mixins import LoginRequiredMixin




class AboutPageView(View,LoginRequiredMixin):
    def get(self, request):
        doctors = Doctor.objects.all()
        services = Service.objects.all()
        appointments = Appointment.objects.all()
        contacts = Contact.objects.all()
        comments = Comments.objects.all()
        context = {
            'doctors': doctors,
            'services': services,
            'appointments': appointments,
            'contacts': contacts,
            'comments': comments,

        }
        return render(request, 'main/about.html',context)


class ServicesPageView(View,LoginRequiredMixin):
    def get(self, request):
        services = Service.objects.all()
        context = {
            'services': services,
        }
        return render(request, 'main/service.html', context)


class ContactPageView(View,LoginRequiredMixin):
    def get(self, request):
        doctors = Doctor.objects.all()
        services = Service.objects.all()
        appointments = Appointment.objects.all()
        contacts = Contact.objects.all()
        comments = Comments.objects.all()
        context = {
            'doctors': doctors,
            'services': services,
            'appointments': appointments,
            'contacts': contacts,
            'comments': comments,

        }
        return render(request, 'main/contact.html',context)


class AppointmentPageView(View,LoginRequiredMixin):
    def get(self, request):
        doctors = Doctor.objects.all()
        services = Service.objects.all()
        appointments = Appointment.objects.all()
        contacts = Contact.objects.all()
        comments = Comments.objects.all()
        context = {
            'doctors': doctors,
            'services': services,
            'appointments': appointments,
            'contacts': contacts,
            'comments': comments,

        }
        return render(request, 'main/appointment.html',context)


from django.shortcuts import render
from django.views import View
from .models import Doctor

class DoctorListView(View,LoginRequiredMixin):
    def get(self, request):
        search = request.GET.get('search', '')
        if search:
            doctors = Doctor.objects.filter(
                first_name__icontains=search
            ) | Doctor.objects.filter(
                last_name__icontains=search
            ) | Doctor.objects.filter(
                category__icontains=search
            )
        else:
            doctors = Doctor.objects.all()

        context = {
            'doctors': doctors,
            'search': search
        }
        return render(request, 'main/doctor.html', context)


class DoctorDetailView(View,LoginRequiredMixin):
    def get(self, request, id):
        doctor = Doctor.objects.get(id=id)
        return render(request,'main/doctor_detail.html',{'doctor':doctor})


class DoctorCreateView(View,LoginRequiredMixin):
    def get(self, request):
        form = DoctorForm()
        return render(request, 'main/doctor_add.html',{'form':form})

    def post(self, request):
        form = DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("doctor-list")
        return render(request, 'main/doctor_add.html', {'form':form})

class DoctorUpdateView(View,LoginRequiredMixin):
    def get(self, request, id):
        return render(request, 'main/doctor_update.html')

    def post(self, request, id):
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_category = request.POST.get('category')

        doctor = Doctor.objects.get(id=id)
        doctor.first_name = new_first_name
        doctor.last_name = new_last_name
        doctor.category = new_category
        doctor.save()
        return redirect("doctor-list")

class DoctorDeleteView(View):
    def get(self, request, id):
        doctor = Doctor.objects.get(id=id)
        doctor.delete()
        return redirect('doctor-list')







class DoctorDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name', ]
    pagination_class = LimitOffsetPagination

class ServiceDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', ]
    pagination_class = LimitOffsetPagination


class AppointmentDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name', 'email' ]
    pagination_class = LimitOffsetPagination

class ContactDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['subject','first_name' ]
    pagination_class = LimitOffsetPagination

class CommentsDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name','comment']
    pagination_class = LimitOffsetPagination





