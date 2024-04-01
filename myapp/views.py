from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TemperatureHumidity
from .serializers import TemperatureHumiditySerializer

@api_view(['POST'])
def temperature_humidity_api(request):
    if request.method == 'POST':
        serializer = TemperatureHumiditySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data received successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
