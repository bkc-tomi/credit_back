from django.urls import path

from . import views

app_name = 'starter'
urlpatterns = [
    path('', views.index, name='index'),
]
