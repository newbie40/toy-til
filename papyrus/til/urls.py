from django.urls import path

from . import views

app_name = 'til'

urlpatterns = [
    path('', views.index, name='index'),
]
