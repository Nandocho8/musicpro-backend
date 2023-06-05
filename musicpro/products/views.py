from django.shortcuts import render

# Create your views here.

#Return hello world in json format

from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({'message': 'Hello, world! with discord webhook'})