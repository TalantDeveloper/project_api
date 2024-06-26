from django.db import models


class Advocate(models.Model):
    username = models.CharField(max_length=200, verbose_name='Username')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

