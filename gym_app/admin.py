from django.contrib import admin
from gym_app.models import FoodTaken, Profile,Food

# Register your models here.
admin.site.register(Profile)
admin.site.register(Food)
admin.site.register(FoodTaken)