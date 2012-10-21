from django.db import models
from shop.models import Product
# class Order(models.Model):
#     BY_CACH = 1;
#     MY_WEB_MONEY = 2;
#     COD = 3;
#     full_name = models.CharField(max_length=60)
#     email = models.CharField(max_length=40)
#     telephone = models.CharField(max_length=40)
#     source_address = models.CharField(max_length=200)
#     form_pay = models.IntegerField()
#     production =  models.CharField(max_length=300)
#     pub_date = models.DateTimeField()
#     def __unicode__(self):
#         return self.full_name

class Bads(Product):
    title = models.CharField(max_length=60)
    cover_picture = models.ImageField(upload_to='img/bads')
    description = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['title']