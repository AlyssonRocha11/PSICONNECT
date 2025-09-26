from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import PsychologistProfile, Appointment

User = get_user_model()
admin.site.register(User)
admin.site.register(PsychologistProfile)
admin.site.register(Appointment)
