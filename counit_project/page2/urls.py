from django.urls import path
from . import views
urlpatterns = [
    path('', views.pag, name='pag'),
]