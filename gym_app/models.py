from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    height=models.IntegerField()
    weight=models.IntegerField()
    category=models.CharField(max_length=50, choices=(('Veg','Veg'),('Non-Veg','Non-veg')))
    goal=models.CharField(max_length=50, choices=(('Gain-Weight','Gain Weight'),('Lose-Weight','Lose Weight')))
    bmi = models.FloatField(default=0, null=False)

    def save(self, *args, **kwargs):
        self.bmi = (self.weight)/(self.height/100)**2
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return "Profile - "+self.user.username

class Food(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=50,choices=(('Veg','Veg'),('Non-Veg','Non-Veg')))
    calories=models.IntegerField()

    def __str__(self):
        return self.name

class FoodTaken(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ingredient1=models.CharField(max_length=50)
    ingredient2=models.CharField(max_length=50)
    ingredient3=models.CharField(max_length=50)
    ingredient4=models.CharField(max_length=50)
    calorie_count=models.IntegerField(default=0)

    def __str__(self):
        return "calorie "+self.user.username
    
