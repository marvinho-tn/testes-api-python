from rest_framework import serializers

# Classe de serialização para conselhos
class AdviceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    advice = serializers.CharField()

# Classe de serialização para contagem de conselhos
class AdviceCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()