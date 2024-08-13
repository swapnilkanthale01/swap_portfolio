from django.db import models

# Create your models here.
class enquiry(models.Model):
    name=models.CharField(max_length=200, null=False, blank=False)
    email=models.CharField(max_length=200, null=False, blank=False)
    mobile_number = models.CharField(max_length=15)
    message=models.TextField()
    
    def __str__(self):
        return self.name