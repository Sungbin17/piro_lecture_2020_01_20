from django.db import models
from django.conf import settings


# Create your models here.

# Customers Table
class Customer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # 외래키 설정
    product = models.CharField(max_length=50)

    def __str__(self):
        return self.product


class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Comment(models.Model):
    content = models.CharField(max_length=250)
    post = models.ManyToManyField(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    intro = models.TextField()
    image_url = models.CharField(null=True, blank=True, max_length=500)

    # def __str__(self):
    #     return self.user

