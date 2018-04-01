from rest_framework import serializers

from api.models import Banner, BannerItem, Image, Theme, Product


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(help_text='图片链接')

    class Meta:
        model = Image
        fields = ('url',)

    def get_url(self, obj):
        if obj.img_from == 2:
            return obj.url
        return self.context['request'].build_absolute_uri('/').strip("/") + '/images' + obj.url


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


class ProductSerializer(serializers.ModelSerializer):
    img = ImageSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'stock', 'price', 'main_img_url', 'summary', 'img')


class ThemeSerializer(serializers.ModelSerializer):
    topic_img = ImageSerializer(read_only=True)
    head_img = ImageSerializer(read_only=True)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Theme
        fields = ('id', 'name', 'description', 'topic_img', 'head_img', 'products')




