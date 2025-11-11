from rest_framework import serializers

class AdviceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    advice = serializers.CharField()

class AdviceCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()