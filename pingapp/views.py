from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def ping(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
    data = request.get('http://ip-api.com/json/' + ip).json()
    if data.get('status') != 'fail':
        return Response({'success': True, 'ip': ip, 'geaodata': data})
    else:
        return Response({'success': True, 'ip': ip})
