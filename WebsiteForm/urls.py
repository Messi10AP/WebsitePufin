from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    #url(r'^$', include('pufin.urls')),
    url(r'^login', include('pufin.urls')),
    url(r'^register', include('pufin.urls')),
    url(r'^pufin', include('pufin.urls')),
    url(r'^admin/', include(admin.site.urls)),	
]
