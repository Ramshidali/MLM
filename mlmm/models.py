from django.db import models
from django.contrib.auth.models import User

class registration(models.Model):
    id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.id.first_name

class wallet(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    wallet_amount = models.IntegerField()


class referel_id(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    reference = models.CharField(max_length=8,null=True,blank=True)


