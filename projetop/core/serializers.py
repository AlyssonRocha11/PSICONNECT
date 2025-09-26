from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PsychologistProfile, Appointment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_psychologist", "cpf", "endereco"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_psychologist", "cpf", "endereco"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            is_psychologist=validated_data.get("is_psychologist", False),
            cpf=validated_data.get("cpf"),
            endereco=validated_data.get("endereco"),
        )
        return user

class PsychologistProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = PsychologistProfile
        fields = ["id", "user", "crp", "bio", "especialidades"]

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["id", "patient", "psychologist", "date", "status"]
