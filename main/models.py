from django.db import models

class ToDo (models.Model):
    text = models.CharField(max_length = 100) # текст задачки нап: купить молоко
    created_at = models.DateField(auto_now_add=True)  # дата
    is_closed = models.BooleanField(default=False) # птичка если задача заверщена
    is_favorite = models.BooleanField(default=False) # задачка важна ли


class BookShop(models.Model):
    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    price = models.FloatField(default=0)
    genre = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    year = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

