from django.urls import path

from . import views

app_name = 'generate_pdf'
urlpatterns = [
    path('', views.index, name='index'),
]
