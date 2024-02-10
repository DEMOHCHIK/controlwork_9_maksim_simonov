from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.forms import AdvertisementForm
from webapp.models import Advertisement


class AdvertisementModeratorListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list_moderator.html'
    context_object_name = 'advertisements'


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advertisement = self.get_object()
        context['comments'] = advertisement.comment_set.order_by(
            '-created_at')
        return context


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    template_name = 'advertisement/create_advertisement.html'
    form_class = AdvertisementForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:index')


class AdvertisementUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertisement
    template_name = 'advertisement/edit_advertisement.html'
    form_class = AdvertisementForm

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != self.request.user:
            return redirect('webapp:index')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('webapp:advertisement_detail', kwargs={'pk': self.object.pk})


class MarkAsPendingDeletionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        advertisement = Advertisement.objects.get(pk=kwargs['pk'])
        if advertisement.author != request.user:
            return redirect('webapp:index')
        advertisement.status = 'Pending deletion'
        advertisement.save()
        return redirect('webapp:index')


class ApproveAdvertisementView(View):
    def post(self, request, *args, **kwargs):
        advertisement = Advertisement.objects.get(pk=kwargs['pk'])
        advertisement.status = 'Published'
        advertisement.save()
        return JsonResponse({'status': 'approved'})


class RejectAdvertisementView(View):
    def post(self, request, *args, **kwargs):
        advertisement = Advertisement.objects.get(pk=kwargs['pk'])
        advertisement.status = 'Rejected'
        advertisement.save()
        return JsonResponse({'status': 'rejected'})
