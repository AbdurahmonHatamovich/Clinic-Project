from django.urls import path
from .views import HomePageView
from .views import LogOutView, dashboard_view, user_register, user_login

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', user_login, name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='user_profile'),
    path('signup/', user_register, name='user_register'),
]



