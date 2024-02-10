from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# urls_api = [
#     path('v1/', include('api_v1.urls'))
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('accounts/', include('accounts.urls')),
    # path('api/', include(urls_api)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
