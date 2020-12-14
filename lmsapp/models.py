from django.db import models


# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    catchoice = [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
    ]
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    category = models.CharField(max_length=30, choices=catchoice, default='education')
    price = models.IntegerField()
    edition = models.IntegerField()

    def __str__(self):
        return self.name
