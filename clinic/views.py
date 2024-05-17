from django.shortcuts import render
from django.views import View
from .models import Appointment,Contact,Service,Doctor,Comments


class HomePageView(View):
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
        return render(request,'main/index.html',context)


class AboutPageView(View):
    def get(self, request):
        return render(request, 'main/about.html')


class ServicesPageView(View):
    def get(self, request):
        return render(request, 'main/service.html')


class ContactPageView(View):
    def get(self, request):
        return render(request, 'main/contact.html')


class AppointmentPageView(View):
    def get(self, request):
        return render(request, 'main/appointment.html')


class DoctorListView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            doctors = Doctor.objects.all()
            context = {
                'doctors': doctors,
                'res': search
            }
            return render(request,'main/doctor_detail.html',context)
        else:
            doctors = Doctor.objects.filter(first_name__icontains=search)
            if doctors:
                doctors = Doctor.objects.all()
                context = {
                    'doctors': doctors,
                    'res': search
                }
                return render(request,'main/doctor_detail.html',context)
            else:
                context = {
                    'doctors': doctors,
                    'res': search
                }
                return render(request,'main/doctor_detail.html',context)

