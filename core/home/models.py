from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField() 
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    
    