from django.db import models

# Create your models here.


class GameDiscount(models.Model):
    gameId = models.IntegerField
    gameInitialPrice = models.IntegerField
    gameFinalPrice = models.IntegerField
    currency = models.CharField(max_length=4)
    discount = models.IntegerField

    def __str__(self):
        return 'Discout: ' + str(self.discount)


class Game(models.Model):
    gameId = models.IntegerField
    gameName = models.CharField(max_length=64)

    def __str__(self):
        return 'Game: ' + str(self.gameName)


class GameImage(models.Model):
    gameId = models.IntegerField
    headImageURL = models.CharField(max_length=128)
    gameImages = models.ArrayField(models.CharField(max_length=128))
