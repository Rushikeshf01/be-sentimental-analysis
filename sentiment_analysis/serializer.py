from rest_framework import serializers


class SentimentAnalysisSerializer(serializers.Serializer):
    sentence = serializers.CharField(max_length=200)
