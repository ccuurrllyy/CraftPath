from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.gis.db import models


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


class Address(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="addresses")
    name = models.CharField(max_length=30)
    location = models.PointField(max_length=40, srid=4326, blank=True, null=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    make_initial_location = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('address-detail', kwargs={'pk': self.pk})


class RouteBestPath(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="best_paths")
    addresses = models.ManyToManyField(Address, blank=True)
    best_path_string = models.CharField(max_length=100, blank=True, null=True)
    best_path_cost = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Best Path: ' + self.route.title + ' - ' + self.best_path_string + ' - ' + str(self.best_path_cost)


class RouteBestPathLocation(models.Model):
    route_best_path = models.ForeignKey(RouteBestPath, on_delete=models.CASCADE, related_name="best_path_locations")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['position']
