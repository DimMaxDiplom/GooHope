from django.db import models

from society.models import Profile

LIKE_STATUS = (
    ('Liked', 'Liked'),
    ('Report', 'Report'),
    ('None', 'None'),
)


class Illustrations(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    likes = models.PositiveIntegerField(blank=True, default=0)
    liked = models.CharField(max_length=8, choices=LIKE_STATUS)


class Videos(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    likes = models.PositiveIntegerField(blank=True, default=0)
    liked = models.CharField(max_length=8, choices=LIKE_STATUS)

    def __str__(self):
        return super(Videos, self).__str__()


class News(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    content = models.TextField()
    likes = models.PositiveIntegerField(blank=True, default=0)
    liked = models.CharField(max_length=8, choices=LIKE_STATUS)


class Reviews(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(blank=True, default=0)
    liked = models.CharField(max_length=8, choices=LIKE_STATUS)
