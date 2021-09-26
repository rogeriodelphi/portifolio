from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name="index"),
]