from django.contrib.auth.models import User
from django.db import models


class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.CharField(max_length=200)
    mnb2pred = models.CharField(max_length=4)
    rfpred = models.CharField(max_length=4)
    decisionpred = models.CharField(max_length=4)
    svmpred = models.CharField(max_length=4)
    knnpred = models.CharField(max_length=4)
    hybrid = models.CharField(max_length=4)
    predicted_date = models.DateTimeField()

    def __str__(self):
        return self.news

    def summary(self):
        return self.news[:100]

    def pub_date_pretty(self):
        return self.predicted_date.strftime('%b %e %y')


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    num = models.IntegerField()
