from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse

# Create your views here.

from pynamodb.connection import TableConnection

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
