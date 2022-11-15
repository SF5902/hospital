# from django.http import JsonResponse
from django.http import HttpResponse
from .models import patientinfo, bedsinfo
from .serializers import PatientSerializer, BedsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])  
def patient_list(request):

    if request.method == 'GET':
        patients_data = patientinfo.objects.all()
        serializer = PatientSerializer(patients_data, many = True)
        return Response(serializer.data)


    if request.method == 'POST':
        data = request.data
        
        if data and data.get("hospital_name", None):
            data['hospital_name'] = bedsinfo.objects.get(hospital_name=data.get("hospital_name", None)).id
        
        serializer = PatientSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
        # ['id','patient_id', 'patient_name', 'disease','medication', 'doctor_name',  'admitted', 'hospital_name']
        # ['id', 'hospital_name','TotalBeds', 'CovidBeds', 'RegularBeds']


            # import pdb; pdb.set_trace()
            x = serializer.data
            if x.get('admitted')== True :
                total_beds= bedsinfo.objects.get(id = x.get('hospital_name'))  #this will be the dictionary access
                if(total_beds.TotalBeds == 0):
                    return Response({"status":"Failed", "message": "No Beds Available"}, status=status.HTTP_400_BAD_REQUEST)
                total_beds.TotalBeds -= 1
                y = serializer.data
                d = y.get('disease')
                d = d.lower()
                if d == "covid":
                    if(total_beds.CovidBeds == 0):
                        return Response({"status":"Failed", "message": "No Beds Available"}, status=status.HTTP_400_BAD_REQUEST)
                    total_beds.CovidBeds -= 1
                else:
                    if(total_beds.RegularBeds == 0):
                        return Response({"status":"Failed", "message": "No Beds Available"}, status=status.HTTP_400_BAD_REQUEST)
                    total_beds.RegularBeds -= 1

            total_beds.save()
            # import pdb; pdb.set_trace()
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)   

    

#---  TO VIEW EACH PATIENT SERIAL WISE

@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, id):
    try:
        patient_data = patientinfo.objects.get(pk=id)
    except patientinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient_data)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PatientSerializer(patient_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
        if serializer.errors:
            return Response({"status":"Failed", "message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status":"Success"}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        patient_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







@api_view(['GET','POST'])  
def beds_list(request):
    if request.method == 'GET':
        beds_data = bedsinfo.objects.all()
        serializer = BedsSerializer(beds_data, many = True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializerbed = BedsSerializer(data = request.data)
        if serializerbed.is_valid():
            serializerbed.save()
            return Response(serializerbed.data, status = status.HTTP_201_CREATED)
        else:
            return HttpResponse("Bad request")

@api_view(['GET', 'PUT', 'DELETE'])
def beds_detail(request, id):
    try:
        beds_data = bedsinfo.objects.get(pk=id)
    except bedsinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BedsSerializer(beds_data)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BedsSerializer(beds_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
        if serializer.errors:
            return Response({"status":"Failed", "message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status":"Success"}, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        beds_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








# from django.http import JsonResponse
# from .models import patientinfo, bedsinfo
# from .serializers import PatientSerializer, BedsSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET','POST'])  
# def patient_list(request):
#     # patient_data = patientinfo.objects.all()
#     # serializer = PatientSerializer(patient_data, many=True)
#     # return JsonResponse({"patient_data":serializer.data}, safe=False)

#     if request.method == 'GET':
#         patients_data = patientinfo.objects.all()
#         serializer = PatientSerializer(patients_data, many = True)
#         return Response(serializer.data)


#     if request.method == 'POST':
#         serializer = PatientSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # updateBedCount(request.data)
#             return Response(serializer.data, status = status.HTTP_201_CREATED)   
    
# def  updateBedCount(data):
#     if(data["disease"].tolowercase() == "covid" and data["admitted"]==True):
#         # BedsSerializer.
#         beds_data = bedsinfo.objects.get(hospital_name=data["hospital_name"])
#         print(beds_data)











# #---  TO VIEW EACH PATIENT SERIAL WISE

# @api_view(['GET', 'PUT', 'DELETE'])
# def patient_detail(request, id):
#     try:
#         patient_data = patientinfo.objects.get(pk=id)
#     except patientinfo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PatientSerializer(patient_data)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = PatientSerializer(patient_data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         if serializer.errors:
#             return Response({"status":"Failed", "message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"status":"Success"}, status=status.HTTP_200_OK)
        
#     elif request.method == 'DELETE':
#         patient_data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







# @api_view(['GET','POST'])  
# def beds_list(request):
#     if request.method == 'GET':
#         beds_data = bedsinfo.objects.all()
#         serializer = BedsSerializer(beds_data, many = True)
#         return Response(serializer.data)


#     if request.method == 'POST':
#         try:
#             serializer = BedsSerializer(data = request.data)
#             print(serializer)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status = status.HTTP_201_CREATED)   
#         # else:
#         #     return Response("rathore indore")
#         except Exception as e:
#             return str(e)

# @api_view(['GET', 'PUT', 'DELETE'])
# def beds_detail(request, id):
#     try:
#         beds_data = bedsinfo.objects.get(pk=id)
#     except bedsinfo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BedsSerializer(beds_data)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = BedsSerializer(beds_data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         if serializer.errors:
#             return Response({"status":"Failed", "message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"status":"Success"}, status=status.HTTP_200_OK)
        
#     elif request.method == 'DELETE':
#         beds_data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


