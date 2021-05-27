from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)       #create 1 - 1 relationship, delete profile if user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

        #override save method to make sure images are not oversized
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) #save initial image

        img = Image.open(self.image.path)   #opens image of current instance

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)   #save resized image, overwrites initial

