from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'ID {self.id} {self.name}'


