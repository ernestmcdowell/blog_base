from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from blog import views
from blog_base import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'images', views.ImageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
