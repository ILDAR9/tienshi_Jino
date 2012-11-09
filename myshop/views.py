from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from shop.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.mail import send_mail, mail_admins
from  shop.shop_api import get_order_from_request

def order_insert(request):
    order = get_order_from_request(request)

    c = Context({
        'name': order,
        })
    return  render_to_response('test.html',c,context_instance=RequestContext(request))

def order_form(request):
    return render_to_response('shop/order_form.html',
        context_instance=RequestContext(request))


def user_check(request):
    return render_to_response('shop/order_commited.html',{
        request.POST.get()
    },
        context_instance=RequestContext(request))

def insert_to_db(request):

    full_name = request.POST['fio']
    costumer_phone = request.POST['telephone']
    products = request.POST['products']
    order = Order(
        full_name=full_name,
        email=request.POST['email'],
        telephone=costumer_phone,
        source_address=request.POST['address'],
        form_pay=request.POST['form_pay'],
        production=products,
        pub_date=timezone.localtime(timezone.now()),
    )
    message = "%s has ordered:\n%s\ntelephone number: %s" % (full_name,products,telephone)
    send_mail('test', message,'nurildar9@gmail.com',['nur-ildar@mail.ru'],fail_silently=TRUE)
    mail_admins(u"only a test",products,fail_silently=False)
    order.save()
    # t = loader.get_template('shop/order_commited.html')
    c = Context({
        'fio': full_name,
        'telephone': costumer_phone,
        'productions': products,
        })
   # return HttpResponse(t.render(c))
    return render_to_response('shop/order_commited.html',c,
    context_instance=RequestContext(request))

def production_show(request):
    products_list = Bads.objects.all()
    return render_to_response('shop/products.html', {'products_list': products_list},
        context_instance=RequestContext(request))
