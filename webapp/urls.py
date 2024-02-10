from django.urls import path

from webapp.views import index

app_name = 'webapp'

urlpatterns = [
    path('', index),
    path('home/', index, name='index'),
]
