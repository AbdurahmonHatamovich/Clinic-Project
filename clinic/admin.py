from django.contrib import admin
from .models import Doctor,Service,Contact,Appointment,Comments
from import_export.admin import ImportExportModelAdmin

@admin.register(Doctor)
class DoctorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'category')
    list_display_links = ('id', 'first_name')
    search_fields = ('id','first_name')


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ('id','name','information')
    list_display_links = ('id','name')
    search_fields = ('id','name')
    ordering=("id",)


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id','first_name','email','subject')
    list_display_links = ('id','first_name')
    search_fields = ('id','first_name')
    ordering=("id",)

@admin.register(Appointment)
class AppointmentAdmin(ImportExportModelAdmin):
    list_display = ('id','first_name','doctor','date')
    list_display_links = ('id','first_name','doctor')
    search_fields = ('id','doctor')
    ordering=('id',)


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id','first_name','last_name','profession')
    list_display_links = ('id','first_name','last_name','profession')
    search_fields = ('id','first_name')
    ordering=('id',)

