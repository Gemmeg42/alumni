from django.db import models


# class Education(models.Model):
#    pass

class Address(models.Model):
    street = models.CharField(max_length=200, blank=False, default='')
    number = models.CharField(max_length=5, blank=False, default='')
    country = models.CharField(max_length=100, blank=False, default='')
    # alumni = models.ForeignKey('Alumni', on_delete=models.CASCADE, related_name='addresses')


class Alumni(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    addresses = models.ManyToManyField(Address)

