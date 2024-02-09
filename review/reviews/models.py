from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    RATING_CHOCIES =((1,1),(2,2),(3,3),(4,4),(5,5))
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    restaurant_name = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOCIES)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    # upload = models.ImageField(upload_to='uploads/')