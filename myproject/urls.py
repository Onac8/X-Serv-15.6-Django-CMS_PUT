from django.conf.urls import include, url
from django.contrib import admin
from cms_put import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'(.+)', views.recurso, name='Se esta haciendo un GET de algo guardado'),
    url(r'', views.main, name='Pagina que habilita hacer un POST'),
]
