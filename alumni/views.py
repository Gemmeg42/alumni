from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from alumni.models import Alumni
from alumni.serializers import AlumniSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def alumni_post(request):
    alumni_data = JSONParser().parse(request)
    alumni_serializer = AlumniSerializer(data=alumni_data)
    if alumni_serializer.is_valid():
        alumni_serializer.save()
        return JsonResponse(alumni_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(alumni_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
