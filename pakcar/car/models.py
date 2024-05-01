from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From ' + self.name + ' ' + self.email


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'Order This {self.product.name} by {self.name}'

