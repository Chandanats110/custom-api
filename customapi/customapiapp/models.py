from django.db import models

class train(models.Model):
    train_no=models.IntegerField()
    train_name=models.CharField(max_length=100)
    start_time=models.TimeField()
    end_time=models.TimeField()
    starting_from=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    food_supply=models.BooleanField(default=False)
    sleeper_price=models.IntegerField()
    general_price=models.IntegerField()
    ac_price=models.IntegerField()
    sleeper_seats=models.IntegerField()
    general_seats=models.IntegerField()
    ac_seats=models.IntegerField()
    img = models.ImageField(upload_to='images/',null=True,blank=True)
