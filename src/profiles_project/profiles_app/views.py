from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Testing the api view"""

    def get(self, request, format=None):
        """Returns a list of strings for testing"""

        api_list = [
            'this is just',
            'for testing',
            'the APIView'
        ]

        return Response({'message': 'Hello', 'items': api_list})
