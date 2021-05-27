from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #  If a user is deleted, their posts also delete

    #this allows you to print the title when you print a post:
    def __str__(self):
        return self.title

        #needed to redirect after post is created:
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) #returns full pat as a string
