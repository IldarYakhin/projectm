from rest_framework import serializers


class LicenseSerializer(serializers.Serializer):
    idlicense = serializers.IntegerField()
    code = serializers.CharField(max_length=11)
    activated = serializers.DateTimeField()
    duration = serializers.IntegerField()