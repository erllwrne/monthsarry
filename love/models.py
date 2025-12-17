from django.db import models

class LoveCard(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lovecards/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Letter(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
