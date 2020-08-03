from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=50)
    academicfee = models.FloatField(default=50000)
    finalexams = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    fathersname = models.CharField(max_length=100, null=True)
    mothersname = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    dateofadmission = models.DateField(null=True)
    roll = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    stuclass = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    fee_paid = models.FloatField(default=0, max_length=10, null=True)
    numofsupplies = models.IntegerField(default=0, null=True)
    gotTc = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class Payment(models.Model):
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    currfeepaid = models.FloatField(max_length=10, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student

