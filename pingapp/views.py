import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def ping(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
    data = requests.get('http://ip-api.com/json/' + ip).json()
    if data.get('status') != 'fail':
        return Response({'success': True, 'ip': ip, 'geodata': data})
    else:
        return Response({'success': True, 'ip': ip})
