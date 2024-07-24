from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id} - {self.name}"


class CarModel(models.Model):
    car_model = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    year_register = models.IntegerField(null=True, blank=True, default=2000)
    insurer = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id} - {self.car_model} - {self.car_color}"


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"


class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.reviewer_name}"
