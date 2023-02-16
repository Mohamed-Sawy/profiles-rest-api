from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
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

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """testing the ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        api_list = [
            'testing',
            'ViewSet'
        ]

        return Response({'message': 'Hello', 'list': api_list})

    def create(self, request):
        serializer = serializers.HelloSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        name = serializer.data.get('name')
        message = f'Hello {name}'
        return Response({'message': message})

    def retrieve(self, request, pk=None):
        return Response({'method': 'RETRIEVE'})

    def update(self, request, pk=None):
        return Response({'method': 'UPDATE'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'PARTIAL_UPDATE'})

    def destroy(self, request, pk=None):
        return Response({'method': 'DESTROY'})
