from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField(default=0)
    ename = models.CharField(max_length=10)
    ecity = models.CharField(max_length=10)

    class Meta:
        db_table = 'myemployees'
