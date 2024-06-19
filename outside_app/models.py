from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    weight = models.FloatField()
    birth_day = models.DateField()
    IIN = models.IntegerField(primary_key=True)


class Child(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    weight = models.FloatField()
    birth_day = models.DateField()
    IIN = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(Human, on_delete=models.CASCADE)


class Icecream(models.Model):
    name = models.CharField(max_length=20)
    TYPES = {
        "C": "Chocolade",
        "V": "Vanila",
        "St": "Strawberry"
    }
    types = models.CharField(max_length=20, choices=TYPES)
    price = models.IntegerField()


class Kiosk_Icecream(models.Model):
    kiosk_name = models.CharField(max_length=20)
    assortment = models.ForeignKey(Icecream, on_delete=models.CASCADE)
    price = models.IntegerField()
