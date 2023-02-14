from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class HelloApiView(APIView):
    """Testing the api view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of strings for testing"""

        api_list = [
            'this is just',
            'for testing',
            'the APIView'
        ]

        return Response({'message': 'Hello', 'items': api_list})

    def post(self, request):
        """create a hello message with the name requested for testing"""

        serializer = serializers.HelloSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        name = serializer.data.get('name')
        message = f'Hello {name}'
        return Response({'message': message})

    def put(self, request, primary_key=None):
        return Response({'method': 'PUT'})

    def patch(self, request, primary_key=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, primary_key=None):
        return Response({'method': 'DELETE'})
