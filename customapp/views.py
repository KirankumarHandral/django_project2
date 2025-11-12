from django.shortcuts import render


from customapp.models import Flight
from customapp.serializer import FlightSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@csrf_exempt
def FlightAPIview(request,id=0):
    if request.method == 'GET':
        flights_data = Flight.objects.all()
        flight_serializer = FlightSerializer(flights_data, many=True)
        return JsonResponse(flight_serializer.data, safe=False)
    elif request.method=="POST":
        flight_data=JSONParser().parse(request)
        flight_serializer=FlightSerializer(data=flight_data)
        if flight_serializer.is_valid():
            flight_serializer.save()
            return JsonResponse("record added successfully",safe=False)
    elif request.method=="PUT":
        flight_data=JSONParser().parse(request)  # old data
        flight=Flight.objects.get(id=flight_data['id'])  # new data
        flight_serializer=FlightSerializer(flight,data=flight_data)
        if flight_serializer.is_valid():
            flight_serializer.save()
            return JsonResponse("record updated successfully",safe=False)
    elif request.method=="DELETE":  
        flight=Flight.objects.get(id=id)
        flight.delete()
        return JsonResponse("record deleted successfully",safe=False)
    
@csrf_exempt
def SAVEFILES(request):
    files = request.FILES.get('file')  # Safely get the 'file' key
    if not files:
        return JsonResponse({'error': 'No file provided'}, status=400)  # Return error if no file is provided
    file_name = default_storage.save(files.name, files)  # Save the file
    return JsonResponse({'file_name': file_name}, safe=False)  # Return the saved file name
   