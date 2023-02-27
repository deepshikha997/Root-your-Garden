from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    img_pro=models.ImageField(upload_to="media", default="default\ppf.png")
    addr_pro=models.TextField( default="lko")
    ph_pro=models.BigIntegerField(default="0905082929")
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.usr.username
 


