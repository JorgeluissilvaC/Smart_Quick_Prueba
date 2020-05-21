from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 50)
    attribute1 = models.CharField(max_length = 50)
    attribute2 = models.CharField(max_length = 50)
    attribute3 = models.CharField(max_length = 50)
    attribute4 = models.CharField(max_length = 50)

    def __str__(self):
        return "%s" % (self.name)