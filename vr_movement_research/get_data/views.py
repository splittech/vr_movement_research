from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import serializers


@api_view(['POST'])
def preset_list(request):
    print(request.data)
    # serializer = serializers.PresetUserSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)