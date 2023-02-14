from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializing a name field to test the api view"""

    name = serializers.CharField(max_length=10)
