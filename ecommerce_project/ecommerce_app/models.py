from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    category_description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to='category_image', blank= True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('ecommerce_app:product_by_category', args=[str(self.slug)])
    
    def __str__(self):
        return str(self.category_name)

class Product(models.Model):
    product_name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    product_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_image',blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('ecommerce_app:ProDetail', args=[self.category.slug,self.slug])
    
    

    class Meta:
        ordering = ('product_name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
   
    def __str__(self):
        return str(self.product_name)