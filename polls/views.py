from django.http import HttpResponse
import json

def index(request):
    test_file = open('data/data.json', 'rb')
    response = HttpResponse(content=test_file)
    response['Content-Type'] = 'application/json'
    return response