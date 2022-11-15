from rest_framework import serializers
from .models import hospital
class HospitalSerializer(serializers. ModelSerializer):
    class Meta:
        model = hospital
        fields = ['id', 'hospital_name', 'department', 'beds_available', 'regular_beds', 'covid_beds']