from django.db import models

# Create your models here.

GENDER_CHOISE=[
    ('M','Male'),
    ('F','Female'),
    ('O','Others')
]


class Student_model(models.Model):
    Sid=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    lastname = models.CharField(max_length=30)
    email=models.EmailField()
    contact=models.CharField(max_length=50)
    gender=models.CharField(choices=GENDER_CHOISE,max_length=128)
    college_name=models.CharField(max_length=40)
    grade = models.CharField(max_length=10)




