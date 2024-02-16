from django.db import models

class Post(models.Model):
    title = models.CharField('заголовок',max_length=50)
    despription = models.TextField('описание')
    created_at = models.DateTimeField('дата создания')
    image = models.CharField('картинки',max_length=200)