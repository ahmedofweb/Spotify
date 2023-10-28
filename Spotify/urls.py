
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from asosiyApp.views import *

router = DefaultRouter()
router.register("izohlar", IzohModelViewSet)
router.register("musics", QoshiqModelViewSet)
router.register("albums", AlbomModelViewSet)
router.register("singers", QoshiqchilarModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('qoshiqchilar/', QoshiqchilarApi.as_view()),
    path('qoshiqchi/<int:pk>/', QoshiqchiApi.as_view()),
    path('albomlar/', AlbomlarApi.as_view()),
    path('albom/<int:pk>/', AlbomApi.as_view()),
    path('qoshiqlar/', QoshiqlarApi.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
