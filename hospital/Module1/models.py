from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.

Blood_Grp=(
    ("1","A-"),
    ("2","A+"),
    ("3","B-"),
    ("4","B+"),
    ("5","AB-"),
    ("6","AB+"),
    ("7","O-"),
    ("8","O+"),
)

Gender=(
    ("1","Male"),
    ("2","Female"),
)


class profilee(models.Model):
    pro=models.OneToOneField(to=User,on_delete=CASCADE,null=True,blank=True)
    profile_image=models.ImageField(upload_to='pic',null=True,blank=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email_id=models.EmailField(max_length=100)
    mobile_number=models.IntegerField()
    gender=models.CharField(max_length=20)
    age=models.IntegerField()
    date_of_birth=models.DateField(null=True,blank=True)
    blood_group=models.CharField(max_length=15,null=True,blank=True)
    city=models.CharField(max_length=40,null=True,blank=True)
    state=models.CharField(max_length=40)
    country=models.CharField(max_length=40,default="India")
    zip_code=models.CharField(max_length=30)
    clinic_name=models.CharField(max_length=50,null=True,blank=True)
    clinic_contact_number=models.IntegerField(null=True,blank=True)
    clinic_address=models.CharField(max_length=100,null=True,blank=True)
    clinic_start_time=models.TimeField(null=True,blank=True)
    clinic_end_time=models.TimeField(null=True,blank=True)
    first_time_consultFees=models.IntegerField(null=True,blank=True)
    second_time_consultFees=models.IntegerField(null=True,blank=True)
    clinic_city_name=models.CharField(max_length=30,null=True,blank=True)
    specialization=models.CharField(max_length=50,null=True,blank=True)
    education=models.CharField(max_length=50,null=True,blank=True)
    experience=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.first_name
