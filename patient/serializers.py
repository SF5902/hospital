from rest_framework import serializers
from .models import patientinfo, bedsinfo
class PatientSerializer(serializers.ModelSerializer):
    # hospital_name = serializers.SerializerMethodField()

    # def get_hospital_name(self, obj):
    #         import pdb; pdb.set_trace()
    #         hospital_name = obj.hospital_name_id
    #         return hospital_name
            

    class Meta:
        model = patientinfo
        fields = ['id', 'patient_name', 'disease','medication', 'doctor_name',  'admitted', 'hospital_name']

class BedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bedsinfo
        fields = ['id', 'hospital_name','TotalBeds', 'CovidBeds', 'RegularBeds']
