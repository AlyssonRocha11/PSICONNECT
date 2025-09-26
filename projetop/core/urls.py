from django.urls import path
from rest_framework import routers
from .views import RegisterView, UserViewSet, PsychologistProfileViewSet, AppointmentViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'psychologists', PsychologistProfileViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
] + router.urls
