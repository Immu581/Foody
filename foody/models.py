from django.db import models


class Users(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    address=models.TextField()



class Own(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=100)

class captains(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=100)

class Veg(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    cost=models.IntegerField()
    quantity=models.IntegerField()


class Snacks(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    cost=models.IntegerField()


class Soft_drinks(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    cost=models.IntegerField()

class Non_veg(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    cost=models.IntegerField()

class Veg_order(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    cost=models.IntegerField()
    quantity=models.IntegerField();
    total=models.IntegerField()

class Non_veg_order(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    cost=models.IntegerField()
    quantity=models.IntegerField();
    total=models.IntegerField()

class Snacks_order(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    cost=models.IntegerField()
    quantity=models.IntegerField();
    total=models.IntegerField()

class Soft_drinks_order(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    cost=models.IntegerField()
    quantity=models.IntegerField();
    total=models.IntegerField()