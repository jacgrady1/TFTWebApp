from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'coolapp.views.work', name='work'),
    url(r'^xiaozu/$', 'coolapp.views.xiaozu', name='about'),
    
)






if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
