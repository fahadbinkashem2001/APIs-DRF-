from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author, related_name='books')
    published_date = models.DateField()

    def __str__(self):
        return self.title

class University(models.Model):
    name = models.CharField(max_length=50,unique=True)
    address = models.TextField(default="")

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=3,decimal_places=2)
    department = models.CharField(max_length=50)
    university = models.ForeignKey(University,on_delete=models.CASCADE,related_name="students")

    def __str__(self):
        return self.name

