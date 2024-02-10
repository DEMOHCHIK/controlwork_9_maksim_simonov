from django.urls import path

from webapp.views import AdvertisementListView

app_name = 'webapp'

urlpatterns = [
    path('', AdvertisementListView.as_view()),
    path('home/', AdvertisementListView.as_view(), name='index'),
]
