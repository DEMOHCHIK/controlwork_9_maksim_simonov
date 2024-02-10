from django.urls import path

from webapp.views import AdvertisementListView, AdvertisementDetailView, AdvertisementCreateView, \
    AdvertisementUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', AdvertisementListView.as_view()),
    path('home/', AdvertisementListView.as_view(), name='index'),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('advertisement/create/', AdvertisementCreateView.as_view(), name='create_advertisement'),
    path('advertisement/<int:pk>/update/', AdvertisementUpdateView.as_view(), name='update_advertisement'),
]
