from core.models import GameDiscount, Game, GameImage
from rest_framework import serializers


class GameDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDiscount
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GameImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameImage
        fields = '__all__'


class PricingSerializer(serializers.Serializer):
    game = GameSerializer(many=True)
    discount = GameDiscountSerializer(many=True)
    gameImage = GameImageSerializer(many=True)
