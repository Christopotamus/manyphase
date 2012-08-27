from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name
