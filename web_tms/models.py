from django.db import models

# Create your models here.

class reg(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	password=models.CharField(max_length=40)
	cpassword=models.CharField(max_length=40)
	mobile=models.BigIntegerField( null=True)
	city=models.CharField(max_length=40)
	address=models.CharField(max_length=40)
	gender= models.CharField(max_length=10, null=True)
	
class god(models.Model):
	name=models.CharField(max_length=40)
	lname=models.CharField(max_length=40)
	mobile=models.BigIntegerField()
	email=models.CharField(max_length=30, null=True)
	truck_type=models.CharField(max_length=40)
	p_city=models.CharField(max_length=40)
	d_city=models.CharField(max_length=40)
	goods=models.CharField(max_length=400)

class cont(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	subject=models.CharField(max_length=40)
	message=models.CharField(max_length=400)


class inqu(models.Model):
	name=models.CharField(max_length=40)
	lname=models.CharField(max_length=40)
	mobile=models.BigIntegerField()
	email=models.CharField(max_length=40)
	subject=models.CharField(max_length=40)
	message=models.CharField(max_length=400)

	

	