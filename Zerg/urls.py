from django.conf.urls import include, url
from django.contrib import admin

from api.views import ProductAPIView, ProductByCategoryAPIView, UserAddressAPIView
from api.viewsets import UserTokenAPIView

urlpatterns = [
    # url(r'^admin/$', admin.site.urls),
    url(r'', include('api.urls')),
    # url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api/v1/token/user', UserTokenAPIView.as_view()),
    url(r'^api/v1/product/recent$', ProductAPIView.as_view()),
    url(r'^api/v1/product/by_category$', ProductByCategoryAPIView.as_view()),
    url(r'^api/v1/product/by_category$', ProductByCategoryAPIView.as_view()),
    url(r'^api/v1/address$', UserAddressAPIView.as_view()),

]
