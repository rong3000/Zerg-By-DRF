import json

import urllib3
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from Zerg import settings
from api.exceptions import WeChatException, ThemeDoesNotExistException
from api.models import Banner, Theme, Product, Category, User
from api.serializer import BannerSerializer, ThemeSerializer, ThemeDetailSerializer, CategorySerializer, \
    ProductDetailSerializer
from api.token import Token
from api.utils import prepare_cached_value, save_to_cache
from api.validators import IdsValidator


class BannerViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
     Banner
     ---

     """
    queryset = Banner.objects.all().prefetch_related('items__img', 'items')
    serializer_class = BannerSerializer


class ThemeViewSet(ReadOnlyModelViewSet):
    """
    ---
    list:
         parameters:
             - name: ids
               description: example id1,id2,id3,id4
               required: false
               type: string
               paramType: query
    """

    def get_queryset(self):
        queryset = Theme.objects.all().prefetch_related('head_img', 'topic_img', 'product', 'product__img')
        ids = self.request.GET.get('ids')
        if ids:
            IdsValidator()(ids)
            queryset = queryset.filter(pk__in=ids.split(','))
            if not queryset.exists():
                raise ThemeDoesNotExistException
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ThemeDetailSerializer
        return ThemeSerializer


class ProductViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.prefetch_related('topic_img')
    serializer_class = CategorySerializer


class UserTokenAPIView(APIView):

    def post(self, request):
        """
        ---
        parameters:
         - name: code
           description: js_code
           required: false
           type: string
           paramType: form
        """

        code = self.request.data.get('code')
        https = urllib3.PoolManager()
        wechat_applets = settings.WECHAT_APPLETS
        response = https.request(
            'GET',
            wechat_applets['LoginURL'],
            fields={
                'appid': wechat_applets['AppID'],
                'secret': wechat_applets['AppSecret'],
                'js_code': code,
                'grant_type': 'authorization_code'
            })
        response = json.loads(response.data.decode())
        if response.get('errcode'):
            raise WeChatException(response['errmsg'])
        openid = response.get('openid', '')
        if openid:
            try:
                user = User.objects.get(openid=openid)
            except User.DoesNotExist:
                user = User.objects.create(openid=openid)
            uid = user.id
            value = prepare_cached_value(response, uid, 16)
            token = Token.generate_token()
            print(token)
            save_to_cache(token, value, 72000)
            return Response(data={'token': token})


