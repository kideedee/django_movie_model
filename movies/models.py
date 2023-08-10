from django.db import models


class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField(default=120)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name
