from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Company, Watchlist
from .serializers import CompanySerializer, WatchlistSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secure_view(request):
    return Response({'message': 'This is a secure view!'})

@api_view(['GET'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def add_to_watchlist(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WatchlistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

