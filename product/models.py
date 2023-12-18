from django.contrib.auth.models import User
from django.db import models

CATEGORY_CHOICES ={
    ('NoteBook', 'NoteBook'),
    ('Pen', 'pen'),
    ('Pencil', 'Pencil'),
    ('Highlighter', 'Highlighter')
}


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_img = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title





class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def total_cost(self):
        return self.quantity * self.price
