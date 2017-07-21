from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def ping(request):
    meta = {}
    for i in request.META:
        meta[i] = str(request.META.get(i))

    return Response({'success': True, 'meta': meta})
