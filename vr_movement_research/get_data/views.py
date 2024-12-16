from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import models, serializers


@api_view(['GET', 'POST'])
def preset_list(request):
    if request.method == 'GET':
        presetUsers = models.PresetUsers.objects.all()
        serializer = serializers.PresetUserListSerializer(presetUsers,
                                                          many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = serializers.PresetUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def preset(request, pk):
    if request.method == 'GET':
        presetUser = models.PresetUsers.objects.get(pk=pk)
        if presetUser:
            serializer = serializers.PresetUserSerializer(presetUser)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        presetUser = models.PresetUsers.objects.get(pk=pk)
        serializer = serializers.PresetUserSerializer(presetUser,
                                                      data=request.data)
        if serializer.is_valid():
            context = serializer.context
            context.update({"pk": pk, "request": request.data})
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        presetUser = models.PresetUsers.objects.filter(pk=pk)
        if presetUser:
            presetUser.delete()
            return Response(status=status.HTTP_200_OK)
        return Response({'id': pk}, status=status.HTTP_400_BAD_REQUEST)
