from django.db import models

from society.models import User


class Dialog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    friend = models.ForeignKey(User, on_delete=models.PROTECT)


class Messages(models.Model):
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    message = models.CharField(max_length=800)
    sender = models.ForeignKey(User, on_delete=models.PROTECT)


class Dialogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
