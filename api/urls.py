from rest_framework.routers import DefaultRouter

from api.viewsets import BannerViewSet, ThemeViewSet

router = DefaultRouter()
router.register(r'^banners', BannerViewSet, base_name='banners')
router.register(r'^themes', ThemeViewSet, base_name='themes')

urlpatterns = router.urls
