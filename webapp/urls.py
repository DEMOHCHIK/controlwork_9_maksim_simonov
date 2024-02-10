from django.urls import path

from webapp.views import AdvertisementListView, AdvertisementDetailView

app_name = 'webapp'

urlpatterns = [
    path('', AdvertisementListView.as_view()),
    path('home/', AdvertisementListView.as_view(), name='index'),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
]
