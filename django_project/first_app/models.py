from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category',max_length=100, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    data = models.DateField(auto_now=True)
    rating = models.PositiveSmallIntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='children', null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
     title = models.CharField(max_length=200)
     author = models.CharField(max_length=200)
     published_date = models.DateField()
     description = models.TextField(null=True, blank=True)

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    net_worth = models.PositiveIntegerField(default=0)
    positive_reviews = models.PositiveIntegerField(default=0)
    books_published = models.PositiveSmallIntegerField(default=0)
    years_experience = models.SmallIntegerField(default=0)
    rating = models.FloatField(default=0)
    average_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


# Create your models here.
