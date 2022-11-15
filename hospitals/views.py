from django.http import JsonResponse
from .models import hospital
from .serializers import HospitalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])  
def hospital_list(request):
    # patient_data = hospital.objects.all()
    # serializer = HospitalSerializer(patient_data, many=True)
    # return JsonResponse({"patient_data":serializer.data}, safe=False)

    if request.method == 'GET':
        hospital_data = hospital.objects.all()
        serializer = HospitalSerializer(hospital_data, many = True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = HospitalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)   
    

#---  TO VIEW EACH PATIENT SERIAL WISE

@api_view(['GET', 'PUT', 'DELETE'])
def hospital_detail(request, id):
    try:
        patient_data = hospital.objects.get(pk=id)
    except hospital.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HospitalSerializer(patient_data)
        return Response(serializer.data)

        
    elif request.method == 'PUT':
        serializer = HospitalSerializer(patient_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
        if serializer.errors:
            return Response({"status":"Failed", "message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status":"Success"}, status=status.HTTP_200_OK)
    


    elif request.method == 'DELETE':
        patient_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
