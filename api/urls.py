from rest_framework.routers import DefaultRouter

from api.viewsets import BannerViewSet, ThemeViewSet, ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'^api/v1/banner', BannerViewSet, base_name='banners')
router.register(r'^api/v1/theme', ThemeViewSet, base_name='themes')
router.register(r'^api/v1/product', ProductViewSet, base_name='products')
router.register(r'^api/v1/category', CategoryViewSet, base_name='categories')


urlpatterns = router.urls

