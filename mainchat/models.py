from django.db import models
from django.db.models.signals import post_save


class Chat(models.Model):
    name = models.CharField(max_length=15, verbose_name="Имя")
    message = models.TextField(verbose_name="Сообщение")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время")


def signal_to_user(sender, **kwargs):
    if kwargs["created"]:
        print("Holaaaaaaaaaaaaaa Amigo")


post_save.connect(signal_to_user, sender=Chat)
