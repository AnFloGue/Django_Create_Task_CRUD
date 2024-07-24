from django.contrib import admin
from .models import Member, CarModel, Task, Review

admin.site.register(Member)
admin.site.register(CarModel)
admin.site.register(Task)
admin.site.register(Review)