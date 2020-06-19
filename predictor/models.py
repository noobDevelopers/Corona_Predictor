from django.db import models


class Predictor(models.Model):
    date = models.CharField(max_length=10)
    PREDICT_CHOICES = (
        ('cases','Active Cases'),
        ('deaths','Deaths'),
        
    )
    to_predict = models.CharField(max_length=20,choices=PREDICT_CHOICES,default='cases')
