from django.db import models

# Create your models here.
class Status(models.Model):
    access = models.IntegerField()
    data_type = models.IntegerField()
    param_index = models.IntegerField()
    param_sub_index = models.IntegerField()
    error_returned = models.IntegerField()
    transfer_value= models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
