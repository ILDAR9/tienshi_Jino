from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template
from shop import urls as shop_urls
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'home.html'}),
    # url(r'^products/',include('shop.urls')),
    url(r'^test$',direct_to_template, {'template':'vopros-otvet.html'}),
    url(r'^vopros-otvet$',direct_to_template,{'template':'vopros-otvet.html'}),
    url(r'^404/', direct_to_template, {'template': '404.html'}),
    url(r'^shop/', include(shop_urls)),
    url(r'^base$', direct_to_template, {'template': 'base.html'}),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

# urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
{'document_root': settings.STATIC_ROOT}),
        (r'^media/static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT  }),
        
    )
