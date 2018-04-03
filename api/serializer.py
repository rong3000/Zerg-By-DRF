from rest_framework import serializers

from api.models import Banner, BannerItem, Image, Theme, Product, Category, ProductProperty, ProductImage, UserAddress


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(help_text='图片链接')

    class Meta:
        model = Image
        fields = ('url',)

    def get_url(self, obj):
        if obj.img_from == 2:
            return obj.url
        return self.context['request'].build_absolute_uri('/').strip("/") + '/images' + obj.url


class ProductImageSerializer(serializers.ModelSerializer):
    img_url = ImageSerializer(source='img', read_only=True)

    class Meta:
        model = ProductImage
        fields = ('img_url', 'order')


class CategorySerializer(serializers.ModelSerializer):
    topic_img = ImageSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'topic_img', 'description')


class BannerItemSerializer(serializers.ModelSerializer):
    img = ImageSerializer(read_only=True)

    class Meta:
        model = BannerItem
        fields = ('key_word', 'type', 'img')


class BannerSerializer(serializers.ModelSerializer):
    items = BannerItemSerializer(many=True, read_only=True)

    class Meta:
        model = Banner
        fields = ('id', 'name', 'description', 'items')


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = ('name', 'detail')


class ProductSerializer(serializers.ModelSerializer):
    main_img_url = serializers.SerializerMethodField()
    img_id = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ('name', 'stock', 'price', 'main_img_url', 'summary', 'img_id')

    def get_main_img_url(self, obj):
        if obj.img.img_from == 2:
            return obj.main_img_url
        return self.context['request'].build_absolute_uri('/').strip("/") + '/images' + obj.main_img_url


class ProductDetailSerializer(ProductSerializer):
    imgs = serializers.SerializerMethodField()
    properties = PropertySerializer(many=True)

    class Meta:
        model = Product
        fields = ('name', 'stock', 'price', 'main_img_url', 'summary', 'img', 'imgs', 'properties')

    def get_imgs(self, obj):
        instance = obj.images.order_by('order')
        return ProductImageSerializer(instance, context=self.context, many=True).data


class ThemeSerializer(serializers.ModelSerializer):
    topic_img = ImageSerializer(read_only=True)
    head_img = ImageSerializer(read_only=True)

    class Meta:
        model = Theme
        fields = ('id', 'name', 'description', 'topic_img', 'head_img')


class ThemeDetailSerializer(serializers.ModelSerializer):
    topic_img = ImageSerializer(read_only=True)
    head_img = ImageSerializer(read_only=True)
    products = ProductSerializer(source='product', read_only=True, many=True)

    class Meta:
        model = Theme
        fields = ('id', 'name', 'description', 'topic_img', 'head_img', 'products')


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('name', 'mobile', 'country', 'province', 'city', 'detail')
