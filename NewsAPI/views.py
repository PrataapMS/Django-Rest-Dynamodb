from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from pynamodb.connection import TableConnection

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from NewsAPI.models import TestExample
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# ------------------------EXAMPLE---------------------------
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# ----------------------------------------------------------


# Create your views here.

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def get_data(request):
    data = TestExample.query("forum-32")
    subj = []
    print ("Help")
    for i in data:
        subj.append(i.subject) 

    print (subj)
    return Response(subj)




def get_example(request):
    """
    List all code snippets, or create a new snippet.
    """
    table = TableConnection('TestExample', host=settings.DYNAMODB_SERVER)
    if request.method == 'GET':
        # Describe the table
    	print(table.describe_table())
        return JsonResponse(table.describe_table(), safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


