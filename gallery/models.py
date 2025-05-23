from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Artist(models.Model):
    ART_STYLE = [
        ('pop', 'pop art'),
        ('graffiti', 'graffiti'),
        ('imp', 'impressionism')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    art_style = models.CharField(max_length=50, choices=ART_STYLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ArtPiece(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    exhibition = models.ForeignKey('Exhibition', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Exhibition(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    short_description = models.TextField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {str(self.start_date)} {str(self.end_date)}'
