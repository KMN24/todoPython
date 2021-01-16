from django.db import models

class ToDo (models.Model):
    text = models.CharField(max_length = 100) # текст задачки нап: купить молоко
    created_at = models.DateField(auto_now_add=True)  # дата
    is_closed = models.BooleanField(default=False) # птичка если задача заверщена
    is_favorite = models.BooleanField(default=False) # задачка важна ли


