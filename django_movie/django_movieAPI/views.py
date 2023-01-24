import json
import os

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_movie.settings import BASE_DIR


data = open(os.path.join(BASE_DIR / 'static/data.json'), 'r')
real_data = json.load(data)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def index(request):
    return Response(real_data)

