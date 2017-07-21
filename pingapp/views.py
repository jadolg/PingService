from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def ping(request):
    return Response({'success': True, 'ip': request.META.get('REMOTE_ADDR', None)})
