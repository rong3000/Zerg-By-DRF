from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, help_text='Banner名称，通常作为标识')
    description = models.CharField(max_length=255, blank=True, null=True, help_text='Banner描述')
    delete_time = models.IntegerField(blank=True, null=True, help_text='删除时间')
    update_time = models.IntegerField(blank=True, null=True, help_text='更新时间')

    class Meta:
        db_table = 'banner'
        verbose_name = 'Banner'
        verbose_name_plural = verbose_name


class BannerItem(models.Model):
    TYPE_CHOICES = (
        (0, '无导向'),
        (1, '导向商品'),
        (2, '导向专题'),
    )
    img = models.OneToOneField('Image', db_constraint=False, help_text='外键，关联image表')
    key_word = models.CharField(max_length=100, help_text='执行关键字，根据不同的type含义不同')
    type = models.IntegerField(choices=TYPE_CHOICES, default=1,
                               help_text='0:无导向；1：导向商品;2:导向专题')
    delete_time = models.IntegerField(blank=True, null=True)
    banner = models.ForeignKey('Banner', db_constraint=False, related_name='items', help_text='外键，关联banner表')
    update_time = models.IntegerField(blank=True, null=True, help_text='更新时间')

    class Meta:
        db_table = 'banner_item'
        verbose_name = 'Banner子项'
        verbose_name_plural = verbose_name


class Category(models.Model):
    name = models.CharField(max_length=50, help_text='分类名称')
    topic_img = models.ForeignKey('Image', db_constraint=False, blank=True, null=True, help_text='外键，关联image表')
    delete_time = models.IntegerField(blank=True, null=True, help_text='删除时间')
    description = models.CharField(max_length=100, blank=True, null=True, help_text='描述')
    update_time = models.IntegerField(blank=True, null=True, help_text='更新时间')

    class Meta:
        db_table = 'category'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name


class Image(models.Model):
    IMG_FROM_CHOICES = (
        (1, '本地'),
        (2, '公网'),
    )
    url = models.CharField(max_length=255, help_text='图片路径')
    img_from = models.IntegerField(db_column='from', choices=IMG_FROM_CHOICES, default=1,
                                   help_text='图片来自 1 本地 ，2公网')
    delete_time = models.IntegerField(blank=True, null=True, help_text='删除时间')
    update_time = models.IntegerField(blank=True, null=True, help_text='更新时间')

    class Meta:
        db_table = 'image'
        verbose_name = '图片'
        verbose_name_plural = verbose_name


class Order(models.Model):
    STATUS_CHOICES = (
        (1, '未支付'),
        (2, '已支付'),
        (3, '已发货'),
        (4, '已支付但库存不足'),
    )
    order_no = models.CharField(unique=True, max_length=20, help_text='订单号')
    user_id = models.IntegerField(help_text='外键，用户id，注意并不是openid')
    delete_time = models.IntegerField(blank=True, null=True, help_text='删除时间')
    create_time = models.IntegerField(blank=True, null=True, help_text='更新时间')
    total_price = models.DecimalField(max_digits=6, decimal_places=2, help_text='总价')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1,
                                 help_text='1:未支付， 2：已支付，3：已发货 , 4: 已支付，但库存不足')
    snap_img = models.CharField(max_length=255, blank=True, null=True, help_text='订单快照图片')
    snap_name = models.CharField(max_length=80, blank=True, null=True, help_text='订单快照名称')
    total_count = models.IntegerField(default=0, help_text='总数')
    update_time = models.IntegerField(blank=True, null=True, help_text='更新时间')
    snap_items = models.TextField(blank=True, null=True, help_text='订单其他信息快照（json)')
    snap_address = models.CharField(max_length=500, blank=True, null=True, help_text='地址快照')
    prepay_id = models.CharField(max_length=100, blank=True, null=True, help_text='订单微信支付的预订单id（用于发送模板消息')

    class Meta:
        db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderProduct(models.Model):
    order = models.ForeignKey('Order', db_constraint=False, help_text='联合主键，订单id')
    product = models.OneToOneField('Product', db_constraint=False, primary_key=True, help_text='联合主键，商品id')
    count = models.IntegerField(help_text='商品数量')
    delete_time = models.IntegerField(blank=True, null=True, help_text='删除时间')
    update_time = models.IntegerField(blank=True, null=True, help_text='更新时间')

    class Meta:
        db_table = 'order_product'
        unique_together = (('product', 'order'),)
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name


class Product(models.Model):
    name = models.CharField(max_length=80, help_text='商品名称')
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text='价格,单位：分')
    stock = models.IntegerField(default=0, help_text='库存量')
    delete_time = models.IntegerField(blank=True, null=True, help_text='删除时间')
    category = models.ForeignKey('Category', db_constraint=False, blank=True, null=True, help_text='商品分类外键')
    main_img_url = models.CharField(max_length=255, blank=True, null=True,
                                    help_text='主图ID号，这是一个反范式设计，有一定的冗余')
    img_from = models.IntegerField(db_column='from', choices=Image.IMG_FROM_CHOICES,
                                   help_text='图片来自 1 本地 ，2公网')
    create_time = models.IntegerField(blank=True, null=True, help_text='创建时间')
    update_time = models.IntegerField(blank=True, null=True, help_text='更新时间')
    summary = models.CharField(max_length=50, blank=True, null=True, help_text='摘要')
    img = models.ForeignKey('Image', db_constraint=False, blank=True, null=True, help_text='图片外键')

    class Meta:
        db_table = 'product'
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class ProductImage(models.Model):
    img = models.ForeignKey('Image', db_constraint=False, help_text='图片外键')
    delete_time = models.IntegerField(blank=True, null=True, help_text='删除时间')
    order = models.IntegerField(help_text='图片排序序号')
    product = models.ForeignKey('Product', db_constraint=False, help_text='商品外键')

    class Meta:
        db_table = 'product_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


class ProductProperty(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, help_text='详情属性名称')
    detail = models.CharField(max_length=255, help_text='详情属性')
    product = models.ForeignKey('Product', db_constraint=False, help_text='商品外键')
    delete_time = models.IntegerField(blank=True, null=True, help_text='删除时间')
    update_time = models.IntegerField(blank=True, null=True, help_text='更新时间')

    class Meta:
        db_table = 'product_property'
        verbose_name = '商品属性'
        verbose_name_plural = verbose_name


class Theme(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    topic_img = models.OneToOneField('Image', related_name='topic', db_constraint=False, blank=True, null=True,
                                     help_text='图片外键')
    delete_time = models.IntegerField(blank=True, null=True)
    head_img = models.OneToOneField('Image', related_name='head', db_constraint=False, blank=True, null=True,
                                    help_text='图片外键')
    update_time = models.IntegerField(blank=True, null=True)
    products = models.ManyToManyField('Product', db_constraint=False, related_name='products', help_text='商品，多对多关系')

    class Meta:
        db_table = 'theme'


class ThirdApp(models.Model):
    app_id = models.CharField(max_length=64)
    app_secret = models.CharField(max_length=64)
    app_description = models.CharField(max_length=100, blank=True, null=True)
    scope = models.CharField(max_length=20)
    scope_description = models.CharField(max_length=100, blank=True, null=True)
    delete_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'third_app'


class User(models.Model):
    openid = models.CharField(unique=True, max_length=50)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    extend = models.CharField(max_length=255, blank=True, null=True)
    delete_time = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'


class UserAddress(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=20)
    province = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    detail = models.CharField(max_length=100, blank=True, null=True)
    delete_time = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(unique=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_address'
