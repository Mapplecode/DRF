from django.contrib.auth.models import User
from django.db import models


STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
]

class Bonds(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    symbol = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Bond'
        verbose_name_plural = 'Bonds'
        db_table = 'tbl_bonds'
        managed = True

    def __str__(self):
        return self.name