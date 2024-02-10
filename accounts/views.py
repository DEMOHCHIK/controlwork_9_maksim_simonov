from django.db.models import Q
from django.shortcuts import redirect, reverse
from django.contrib.auth import login, get_user_model
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import MyUserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView

from webapp.models import Advertisement


class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'user_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')
        if not next_page:
            next_page = reverse('webapp:index')

        return next_page


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        if self.request.user == user:
            context['advertisements'] = Advertisement.objects.filter(author=user).exclude(status='Pending deletion')
        else:
            context['advertisements'] = Advertisement.objects.filter(author=user, status='Published')
        return context


class UserChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user_password_change.html'

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.request.user.pk})
