from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# class AdminView(APIView):
#     # keycloak_scopes = {'GET': 'read-only-admin-view',
#     #                    'POST': 'edit-admin-view'}
@login_required
@api_view(['GET', 'POST'])
def API_view(request):
    if request.method == 'GET':
        return HttpResponse('Secure page. <a href="/openid/logout">Logout</a>')
    elif request.method == 'POST':
        return JsonResponse({"page": "Edit Admin Resource"})
   
