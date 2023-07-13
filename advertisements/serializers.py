from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context['request'].user
        creator = Advertisement.objects.filter(creator=user, status='OPEN').count()
        method = self.context['request'].method
        if creator >=10 and method == 'POST':
            raise ValidationError("Превышено максимальное количество объявлений")
        return data
            


        
