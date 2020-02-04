from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title