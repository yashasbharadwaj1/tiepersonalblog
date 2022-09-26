from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""
This is used when one record of a model A is related to exactly one record of another model B.
here a one user has to have a single profile 

models.Cascade because This is the default value. It automatically deletes all the related records when a record is deleted.
(e.g. when an profile record is deleted user record related to it will be deleted)
"""
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user=models.IntegerField(default=0)

    def __str__(self):
        return f'Profile for user {self.user.username}'
