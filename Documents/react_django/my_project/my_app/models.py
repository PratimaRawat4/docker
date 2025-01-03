from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('shirts', 'Shirts'),
        ('pants', 'Pants'),
        ('jackets', 'Jackets'),
        ('accessories', 'Accessories'),
        ('sportswear', 'Sportswear'),
        ('bags', 'Bags'),
        ('watches', 'Watches'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    year = models.IntegerField()
    category = models.CharField(max_length=500, choices=CATEGORY_CHOICES, default='shoes')
    image = models.ImageField(null=True, blank=True)
    rating = models.FloatField(default=0.0) 

    def __str__(self):
        return self.name



