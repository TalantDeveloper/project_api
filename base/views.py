from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from .serializers import AdvocateSerializer


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)


@api_view(['GET'])
def advocate_list(request):
    data = ['botir', 'shaxzod', 'sobir']
    advocates = Advocate.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def advocate_details(request, username):
    advocate = Advocate.objects.get(username=username)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
