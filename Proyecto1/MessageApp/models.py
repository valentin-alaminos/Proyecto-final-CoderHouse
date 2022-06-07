from django.db import models

class message (models.Model):
    message = models.CharField(max_length=255)
    emisor = models.CharField(max_length=255)
    receptor = models.CharField(max_length=255)
    date = models.DateTimeField(default=None)
    def __str__(self):
        return self.message
