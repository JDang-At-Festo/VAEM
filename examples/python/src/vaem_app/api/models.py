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

class VaemState(models.Model):
    status = models.IntegerField()
    error = models.IntegerField()
    readiness = models.IntegerField()
    operating_mode = models.IntegerField()
    valve1 = models.IntegerField()
    valve2 = models.IntegerField()
    valve3 = models.IntegerField()
    valve4 = models.IntegerField()
    valve5 = models.IntegerField()
    valve6 = models.IntegerField()
    valve7 = models.IntegerField()
    valve8 = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
