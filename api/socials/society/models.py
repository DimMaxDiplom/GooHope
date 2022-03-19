from django.db import models


class User(models.Model):
    publicity_choices = (
        ('ALL', 'All'),
        ('FaF', 'Friend and friends of friends'),
        ('JF', 'Just friends'),
        ('OO', 'Only owner')
    )
    user_id = models.IntegerField(unique=True)
    avatar = models.ImageField(upload_to=f'user_{user_id}/', blank=True, null=True, default=None)
    status = models.BooleanField(default=True)
    publicity = models.CharField(choices=publicity_choices)


class Society(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField()
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500, null=True, blank=True)


class SocietyMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)


class SocietyComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    comment = models.CharField(max_length=230)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
