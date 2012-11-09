# -*- coding: utf-8 -*-
from myshop.models import Bads
from django.contrib import admin
#from shop.models import Product

#class BadsAdmin(admin.StackedInline):
##    model=Bads
#
#    fieldsets = [
##        ('Common',{'fields':['name','slug','unit_price','active']}),
#        ('Тип припарата:\n1-БАДЫ\n2-КРАСОТА\n3-ПРИБОРЫ\n4-БЫТОВАЯ ХИМИЯ',  {'fields': ['type']}),
#        ('Колличество препаратов',{'fields':['package_amount']}),
#        ('Фото препарата',{'fields':['cover_picture']}),
#        ('Короткое описание для списка',{'fields':['short_description']}),
#        ('Полное описанпие',{'fields':['long_description']}),
#    ]
#class ProductMain(admin.ModelAdmin):
##    fields = ['name','slug','unit_price','active']
#    inlines = [BadsAdmin]
#
#
#
#admin.site.register(Product, ProductMain)
admin.site.register(Bads)