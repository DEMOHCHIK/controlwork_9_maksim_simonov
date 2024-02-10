from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.forms import AdvertisementForm
from webapp.models import Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/index.html'
    context_object_name = 'published_ads'

    def get_queryset(self):
        return Advertisement.objects.filter(status='Published').order_by('-published_at')


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisement/detail.html'
    context_object_name = 'advertisement'


class AdvertisementCreateView(CreateView):
    model = Advertisement
    template_name = 'advertisement/create_advertisement.html'
    form_class = AdvertisementForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:index')


class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    template_name = 'advertisement/edit_advertisement.html'
    form_class = AdvertisementForm

    def get_success_url(self):
        return reverse_lazy('webapp:advertisement_detail', kwargs={'pk': self.object.pk})
