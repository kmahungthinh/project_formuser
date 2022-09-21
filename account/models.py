from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    la_khachhang = models.BooleanField(default=False)
    la_nhanvien= models.BooleanField(default=False)
    makhachhang = models.CharField(max_length=100, default='')
    madinhdanh = models.CharField(max_length=100, default='')
    motanoidungyeucau = models.CharField(max_length=100,default='')
    soluongkhaosat = models.IntegerField(default=0)
    socaukhaosat = models.IntegerField(default=0)
    password_ro = models.CharField(max_length=100)
    sodienthoai = models.CharField(max_length=12)
    diachi = models.CharField(max_length=100)