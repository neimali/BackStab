from rest_framework import serializers
from core.models import GameDiscount

class GameDiscountSerilizers(serializers.ModelSerializer):

    class Meta:
        model = GameDiscount
        fields = (
            'gameId',
            'gameInitialPrice',
            'gameFinalPrice',
            'currency',
            'discount'
        )
