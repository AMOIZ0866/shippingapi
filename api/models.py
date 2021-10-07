import os
from datetime import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    phone = models.CharField(max_length=17, unique=True, primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=8, blank=True, null=True)
    verified = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.phone


class PhoneOTP(models.Model):
    phone = models.CharField(max_length=17)
    otp = models.CharField(max_length=250,blank=False, null=True)
    logged = models.BooleanField(default=False)

    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)


class Dispatches(models.Model):
    dis_id = models.AutoField(auto_created=True, primary_key=True)
    dis_rep = models.CharField(max_length=100)
    dis_wieght = models.IntegerField()
    dis_dimen = models.CharField(max_length=20)
    dis_packages = models.IntegerField()
    commodity = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    dis_status = models.CharField(max_length=10)


class Pickups(models.Model):
    dis_id = models.ForeignKey(Dispatches, related_name='pickup', on_delete=models.CASCADE)
    pick_location = models.CharField(max_length=200)
    p_action = models.CharField(max_length=20)
    p_arv_date = models.DateTimeField()
    p_dep_date = models.DateTimeField()


class Deliveries(models.Model):
    dis_id = models.ForeignKey(Dispatches, related_name='deliveries', on_delete=models.CASCADE)
    dev_location = models.CharField(max_length=200)
    dev_action = models.CharField(max_length=20)
    dev_arv_date = models.DateTimeField()
    dev_dep_date = models.DateTimeField()








