from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=20)

class Course(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)