from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug          = models.SlugField(max_length=100,unique=True )
    description   = models.TextField(blank=True)
    cat_image     = models.ImageField(upload_to='photos/categories', blank=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'Categories'


    def __str__(self):
        return self.category_name
