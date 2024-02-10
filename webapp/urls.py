from django.urls import path

from webapp.views import AdvertisementListView, AdvertisementModeratorListView, AdvertisementDetailView, \
    AdvertisementCreateView, AdvertisementUpdateView, MarkAsPendingDeletionView, CommentCreateView, CommentDeleteView, \
    ApproveAdvertisementView, RejectAdvertisementView

app_name = 'webapp'

urlpatterns = [
    path('', AdvertisementListView.as_view()),
    path('home/', AdvertisementListView.as_view(), name='index'),
    path('advertisement_list_moderator/', AdvertisementModeratorListView.as_view(), name='moderator_list'),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('advertisement/create/', AdvertisementCreateView.as_view(), name='create_advertisement'),
    path('advertisement/<int:pk>/update/', AdvertisementUpdateView.as_view(), name='update_advertisement'),
    path('advertisement/<int:pk>/mark_as_pending_deletion/', MarkAsPendingDeletionView.as_view(),
         name='mark_as_pending_deletion'),
    path('advertisement/<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('advertisement/<int:pk>/approve/', ApproveAdvertisementView.as_view(), name='approve_advertisement'),
    path('advertisement/<int:pk>/reject/', RejectAdvertisementView.as_view(), name='reject_advertisement'),
]
