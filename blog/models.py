from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Route(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now, blank=True, null=True)
    number_of_locations = IntegerRangeField(min_value=2, max_value=50, default=None, blank=True, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('route-detail', kwargs={'pk': self.pk})

class City(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Area(models.Model):
    city= models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Address(models.Model):
    route_name = models.ForeignKey(Route, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, blank=True, null=True)
    latitude= models.FloatField(max_length=30, default=None,blank=True, null=True)
    longitude= models.FloatField(max_length=30, default=None,blank=True,null=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('address-detail', kwargs={'pk': self.pk})
