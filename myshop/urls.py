from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('shop.views',
    url(r'^order_insert$', 'insert_to_db'),
    url(r'^user_check$', 'user_check'),
    url(r'^order_form$', 'order_form'),#direct_to_template, {'template': 'shop/order_form.html', }),
    url(r'^bads$', direct_to_template, {'template': 'myshop/products.html', }),),
