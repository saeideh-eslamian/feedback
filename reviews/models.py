from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=50)
    text_review = models.TextField()
    rating = models.IntegerField()
