from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/index.html'
    context_object_name = 'published_ads'

    def get_queryset(self):
        return Advertisement.objects.filter(status='Published').order_by('-published_at')
