from django.db import models


class Country(models.Model):
    """
        Manages country objects
    """
    name = models.CharField(max_length=100, primary_key=True)
    code = models.CharField(max_length=30, blank=False, unique=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    """
        Manages states objects
    """
    name = models.CharField(max_length=100, primary_key=True)
    code = models.CharField(max_length=30, blank=False, unique=True)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    """
        Manages city objects
    """
    name = models.CharField(max_length=100, primary_key=True)
    code = models.CharField(max_length=30, blank=False, unique=True)
    state = models.ForeignKey(State,on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return self.name


class Address(models.Model):
    """
        Manages address objects
    """
    street = models.CharField(max_length=201, primary_key=True)
    zipcode = models.CharField(max_length=30, blank=False, unique=True)
    city = models.ForeignKey(City,on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State,on_delete=models.DO_NOTHING, default=None)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING, default=None)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self) -> str:
        return f"{self.street}, {self.zipcode}, {self.city}"
