from django.db import models

# Create your models here.
class Clients(models.Model):
    document = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)

    def __str__(self):
        return "%s" % (self.document)
