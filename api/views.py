from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.exceptions import ProductDoesNotExistException, ParameterException, TokenInvalidException, UserException
from api.models import Product, User, UserAddress
from api.serializer import ProductSerializer, UserAddressSerializer
from api.utils import get_current_uid, SUCCESS_MESSAGE
from api.validators import CountValidator


class ProductAPIView(APIView):

    def get(self, request):
        """
        ---
         parameters:
             - name: count
               description: The new products count ;  15
               required: false
               type: string
               paramType: query
        """
        count = request.GET.get('count', 15)
        count = CountValidator()(count)
        queryset = Product.objects.order_by('-create_time')[:count]
        if not queryset.exists():
            raise ProductDoesNotExistException
        data = ProductSerializer(queryset, many=True, context={'request': request}).data
        return Response(data=data, status=201)


class ProductByCategoryAPIView(APIView):

    def get(self, request):
        """
        ---
         parameters:
             - name: category_id
               description: TThe products category_id
               required: false
               type: string
               paramType: query
        """
        category_id = request.GET.get('category_id', '')
        if category_id == 0 or not str(category_id).isdigit():
            raise ParameterException('category_id 为正整数')

        queryset = Product.objects.filter(category_id=category_id)
        if not queryset.exists():
            raise ProductDoesNotExistException('指定分类下的商品不存在')
        data = ProductSerializer(queryset, many=True, context={'request': request}).data
        return Response(data=data, status=201)


class UserAddressAPIView(APIView):

    def post(self, request):
        """
        ---
         parameters:
             - name: name
               description: 姓名
               required: false
               type: string
               paramType: form
             - name: mobile
               description: 手机号
               required: false
               type: string
               paramType: form
             - name: country
               description: 国家
               required: false
               type: string
               paramType: form
             - name: province
               description: 省
               required: false
               type: string
               paramType: form
             - name: city
               description: 城市
               required: false
               type: string
               paramType: form
             - name: detail
               description: 详细地址
               required: false
               type: string
               paramType: form
        """
        token = request.META.get('token', '6619e553a1d9c55eed748f7cf3bd6b99')
        if not token:
            raise TokenInvalidException('请在header携带token访问该接口')
        uid = get_current_uid(token)
        try:
            User.objects.get(id=uid)
        except User.DoesNotExist:
            raise UserException
        instance = UserAddress.objects.get_or_create(user_id=uid)[0]
        serializer = UserAddressSerializer(instance=instance, data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(data=SUCCESS_MESSAGE, status=201)
