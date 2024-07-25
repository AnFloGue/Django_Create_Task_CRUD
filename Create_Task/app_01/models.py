from django.db import models


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
