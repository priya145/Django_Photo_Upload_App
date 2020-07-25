from django.db import models

from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone




class Photo(models.Model):
    photo_uploader=models.ForeignKey(User, on_delete=models.CASCADE, blank=True , null=False)
    document= models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo_uploader.username
    
    

 
