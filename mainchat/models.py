from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=15, verbose_name="Имя")
    message = models.TextField(verbose_name="Сообщение")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время")
