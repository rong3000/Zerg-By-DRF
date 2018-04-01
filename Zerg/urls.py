from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'', include('api.urls')),
    url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),

]
