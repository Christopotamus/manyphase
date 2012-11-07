from django.db import models
from django.forms import ModelForm

# Create your models here.
class Customer(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    url = models.CharField(max_length=255)
    comments = models.TextField()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class PartialCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('email',)

class FullCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields =('email', 'first_name','last_name','url','comments')
