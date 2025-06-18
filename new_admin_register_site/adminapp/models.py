from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name

class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)


class Group(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=False)
    age = models.IntegerField(null=True, blank=False)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images', null=True)
