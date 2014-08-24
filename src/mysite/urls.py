from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'coolapp.views.home', name='home'),
    url(r'^about/$', 'coolapp.views.about', name='about'),
    url(r'^work/$', 'coolapp.views.work', name='work'),
    url(r'^contact/$', 'coolapp.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)






if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
    