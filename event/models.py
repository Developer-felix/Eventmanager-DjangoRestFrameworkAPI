from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.title
    
