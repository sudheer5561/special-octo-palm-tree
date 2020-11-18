from django.db import models


class ShortLink(models.Model):
    short = models.CharField(max_length=255, unique=True)
    full = models.CharField(max_length=10000)

    def __str__(self):
        return "{self.short} -> {self.full}".format(self=self)
