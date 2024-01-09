from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    text = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name