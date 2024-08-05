from rest_framework import serializers
from .models import BookRecommendation


class BookRecommendationSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = BookRecommendation
        fields = ["id", "user", "user_name", "title", "author", "created_at"]

    def get_user_name(self, obj):
        return obj.user.username
