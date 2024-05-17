from django.db import models
from django.forms import EmailField


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/doctors/')
    category = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id']),
        ]


class Service(models.Model):
    name = models.CharField(max_length=100)
    information = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id']),
        ]



class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id']),
        ]


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    email = EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id']),
        ]


class Comments(models.Model):
    comment = models.TextField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patient_image = models.ImageField(upload_to='media/comments/')
    profession = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id']),
        ]







