from django.db import models
from apps.client.models import Clients
from apps.product.models import Products
# Create your models here.

class Bills(models.Model):
    name = models.CharField(max_length = 50)
    client_id = models.ForeignKey (Clients, null = True, blank = True, on_delete = models.CASCADE)
    company_name = models.CharField(max_length = 50)
    nit = models.CharField(max_length = 50)
    code = models.CharField(max_length = 50)
    product = models.ManyToManyField(Products)

    def __str__(self):
        return "%s" % (self.name)
