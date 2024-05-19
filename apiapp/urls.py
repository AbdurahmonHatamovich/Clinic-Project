from django.urls import path, include
from clinic.views import ( AboutPageView, ServicesPageView, ContactPageView, AppointmentPageView,
                     CommentsDetailApiView, AppointmentDetailApiView, ServiceDetailApiView, ContactDetailApiView, DoctorDetailApiView,DoctorListView,DoctorDetailView,DoctorCreateView,DoctorUpdateView,DoctorDeleteView)
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Clinic API",
        description="Clinic Application demo",
        default_version="v1",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='muruvat@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

router = routers.DefaultRouter()
router.register('doctor', DoctorDetailApiView, basename='doctor')
router.register('comment', CommentsDetailApiView, basename='comment')
router.register('contact', ContactDetailApiView, basename='contact')
router.register('appointment', AppointmentDetailApiView, basename='appointment')
router.register('service', ServiceDetailApiView, basename='service')

urlpatterns = [
    path('', include(router.urls)),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
    ]