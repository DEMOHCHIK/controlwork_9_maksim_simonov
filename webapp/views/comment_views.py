from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from webapp.models import Advertisement, Comment


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        text = request.POST.get('text')
        advertisement = get_object_or_404(Advertisement, pk=pk)
        user = request.user
        Comment.objects.create(text=text, advertisement=advertisement, author=user)
        return redirect('webapp:advertisement_detail', pk=pk)


class CommentDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        advertisement_pk = comment.advertisement.pk
        if request.user == comment.author:
            comment.delete()
            return redirect('webapp:advertisement_detail', pk=advertisement_pk)
        else:
            return HttpResponseForbidden("Вы не можете удалить этот комментарий")
