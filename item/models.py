from django.db import models
from django.contrib.auth.models import User  # Pastikan ini di-import

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)  # Perbaiki typo dan format tuple
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)  # Perbaiki typo
    created_at = models.DateTimeField(auto_now_add=True)  # Tambahkan spasi

    def __str__(self):
        return self.name  # Tambahkan method __str__ untuk representasi yang lebih baik