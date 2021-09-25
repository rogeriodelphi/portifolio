from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastros/vacinas/', include('apps.accounts.urls')),
]


admin.site.site_header = "LICAMB - Sistema de Licenciamento"
admin.site.site_title = "LICAMB - Sistema de Licenciamento"
admin.site.index_title = "LICAMB - Sistema de Licenciamento"