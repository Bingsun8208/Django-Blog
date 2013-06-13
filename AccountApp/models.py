from django.db import models

# Create your models here.

class accounts(models.Model):
    accountId = models.CharField(primary_key=True, max_length=32)
    accountPwd = models.CharField(max_length=200)
    accountName = models.CharField(max_length=200)
    createDate = models.DateTimeField()
    email = models.EmailField()