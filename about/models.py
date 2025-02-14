from django.db import models

# Create your models here.

class About(models.Model):
    """
    Stores a single About text entry
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - updated on {self.updated_on}"