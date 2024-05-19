from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from clinic.models import Appointment,Doctor,Service,Contact,Comments

from .models import Category
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist


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
class LogOutView(View):
    def get(self, request):
        return render(request, 'main/logged_out.html')


def user_login(request):
    global categories
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Your profile is not active')
            else:
                return HttpResponse('There is an error in the login or password')
    else:
        form = LoginForm()
        categories = Category.objects.all()
    context = {
        'form': form,
        'categories': categories

    }
    return render(request, 'main/login.html', context)


@login_required
def dashboard_view(request):
    user = request.user
    profile_info = user.profile
    categories = Category.objects.all()
    context = {
        'user': user,
        'profile': profile_info,
        'categories': categories
    }
    return render(request, 'main/user_profile.html', context)



def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            categories = Category.objects.all()
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {
                'new_user': new_user,
                'categories': categories
            }
            return render(request, 'main/register_done.html', context)
        else:
            # Return an error response if the form is not valid
            context = {
                'user_form': user_form
            }
            return render(request, 'main/register.html', context)
    else:
        user_form = UserRegistrationForm()
        categories = Category.objects.all()
        context = {
            'user_form': user_form,
            'categories': categories
        }
        return render(request, 'main/register.html', context)





