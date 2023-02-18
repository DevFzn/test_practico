from django.db import models

# Nota: Los valores máximos admitidos deben ser optimizados.

class Network(models.Model):
    id_network = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    gbfs_href = models.CharField(max_length=255)
    href = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

class Station(models.Model):
    id_station = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    timestamp = models.DateTimeField()
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Extra(models.Model):
    address = models.CharField(max_length=255)
    altitude = models.FloatField()
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_updated = models.IntegerField()
    normal_bikes = models.IntegerField()
    payment = models.CharField(max_length=255)
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=255)
    renting = models.IntegerField()
    returning = models.IntegerField()
    slots = models.IntegerField()
    uid = models.CharField(max_length=255)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
