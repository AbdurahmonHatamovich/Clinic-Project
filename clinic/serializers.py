from rest_framework import serializers
from .models import Service,Comments,Contact,Doctor,Appointment


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','first_name','category']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','name']


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = ['id','first_name','email','doctor']



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','first_name','email','subject']



class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id','comment','first_name','profession']








