from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class GameDiscount(models.Model):
    gameId = models.IntegerField(default=0)
    gameInitialPrice = models.IntegerField(default=0)
    gameFinalPrice = models.IntegerField(default=0)
    currency = models.CharField(max_length=4, default='ca')
    discount = models.IntegerField(default=0)

    def __str__(self):
        return 'Discout: ' + str(self.discount)


class Game(models.Model):
    gameId = models.IntegerField(default=0)
    gameName = models.CharField(max_length=256)

    def __str__(self):
        return 'Game: ' + str(self.gameName)


class GameImage(models.Model):
    gameId = models.IntegerField(default=0)
    headImageURL = models.CharField(max_length=256)
    gameImages = ArrayField(models.CharField(max_length=256, null=True), null=True)
