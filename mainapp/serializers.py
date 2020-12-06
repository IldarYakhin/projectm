from rest_framework import serializers
from .models import License


class GetLicenseSerializer(serializers.Serializer):
    idlicense = serializers.IntegerField()
    code = serializers.CharField(max_length=11)
    activated = serializers.DateTimeField()
    duration = serializers.IntegerField()

    class Meta:
        model = License
        fields = ('code', 'duration',)

    def create(self, validated_data):
        return License.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.duration = validated_data.get('duration', instance.duration)
        return instance


class PostLicenseSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=11)
    duration = serializers.IntegerField()

    class Meta:
        model = License
        fields = ('code', 'duration',)

    def create(self, validated_data):
        return License.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.duration = validated_data.get('duration', instance.duration)
        return instance