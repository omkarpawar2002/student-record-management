from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    course_purchase = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=100)
    is_graduate = models.BooleanField(default=False)
