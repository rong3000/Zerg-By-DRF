# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, help_text='Banner名称，通常作为标识', max_length=50)),
                ('description', models.CharField(null=True, blank=True, help_text='Banner描述', max_length=255)),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
            ],
            options={
                'db_table': 'banner',
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
            },
        ),
        migrations.CreateModel(
            name='BannerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('key_word', models.CharField(help_text='执行关键字，根据不同的type含义不同', max_length=100)),
                ('type', models.IntegerField(default=1, help_text='0:无导向；1：导向商品;2:导向专题', choices=[(0, '无导向'), (1, '导向商品'), (2, '导向专题')])),
                ('delete_time', models.IntegerField(null=True, blank=True)),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('banner', models.ForeignKey(to='api.Banner', help_text='外键，关联banner表', related_name='items', db_constraint=False)),
            ],
            options={
                'db_table': 'banner_item',
                'verbose_name': 'Banner子项',
                'verbose_name_plural': 'Banner子项',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(help_text='分类名称', max_length=50)),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('description', models.CharField(null=True, blank=True, help_text='描述', max_length=100)),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
            ],
            options={
                'db_table': 'category',
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(help_text='图片路径', max_length=255)),
                ('img_from', models.IntegerField(default=1, db_column='from', help_text='图片来自 1 本地 ，2公网', choices=[(1, '本地'), (2, '公网')])),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
            ],
            options={
                'db_table': 'image',
                'verbose_name': '图片',
                'verbose_name_plural': '图片',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('order_no', models.CharField(unique=True, help_text='订单号', max_length=20)),
                ('user_id', models.IntegerField(help_text='外键，用户id，注意并不是openid')),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('create_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('total_price', models.DecimalField(max_digits=6, help_text='总价', decimal_places=2)),
                ('status', models.IntegerField(default=1, help_text='1:未支付， 2：已支付，3：已发货 , 4: 已支付，但库存不足', choices=[(1, '未支付'), (2, '已支付'), (3, '已发货'), (4, '已支付但库存不足')])),
                ('snap_img', models.CharField(null=True, blank=True, help_text='订单快照图片', max_length=255)),
                ('snap_name', models.CharField(null=True, blank=True, help_text='订单快照名称', max_length=80)),
                ('total_count', models.IntegerField(default=0, help_text='总数')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('snap_items', models.TextField(null=True, blank=True, help_text='订单其他信息快照（json)')),
                ('snap_address', models.CharField(null=True, blank=True, help_text='地址快照', max_length=500)),
                ('prepay_id', models.CharField(null=True, blank=True, help_text='订单微信支付的预订单id（用于发送模板消息', max_length=100)),
            ],
            options={
                'db_table': 'order',
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(help_text='商品名称', max_length=80)),
                ('price', models.DecimalField(max_digits=6, help_text='价格,单位：分', decimal_places=2)),
                ('stock', models.IntegerField(default=0, help_text='库存量')),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('main_img_url', models.CharField(null=True, blank=True, help_text='主图ID号，这是一个反范式设计，有一定的冗余', max_length=255)),
                ('img_from', models.IntegerField(db_column='from', help_text='图片来自 1 本地 ，2公网', choices=[(1, '本地'), (2, '公网')])),
                ('create_time', models.IntegerField(null=True, blank=True, help_text='创建时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('summary', models.CharField(null=True, blank=True, help_text='摘要', max_length=50)),
            ],
            options={
                'db_table': 'product',
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('order', models.IntegerField(help_text='图片排序序号')),
                ('img', models.ForeignKey(to='api.Image', db_constraint=False, help_text='图片外键')),
            ],
            options={
                'db_table': 'product_image',
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, help_text='详情属性名称', max_length=30)),
                ('detail', models.CharField(help_text='详情属性', max_length=255)),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
            ],
            options={
                'db_table': 'product_property',
                'verbose_name': '商品属性',
                'verbose_name_plural': '商品属性',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(null=True, blank=True, max_length=255)),
                ('delete_time', models.IntegerField(null=True, blank=True)),
                ('update_time', models.IntegerField(null=True, blank=True)),
                ('head_img', models.OneToOneField(to='api.Image', null=True, blank=True, related_name='head', db_constraint=False, help_text='图片外键')),
            ],
            options={
                'db_table': 'theme',
            },
        ),
        migrations.CreateModel(
            name='ThirdApp',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('app_id', models.CharField(max_length=64)),
                ('app_secret', models.CharField(max_length=64)),
                ('app_description', models.CharField(null=True, blank=True, max_length=100)),
                ('scope', models.CharField(max_length=20)),
                ('scope_description', models.CharField(null=True, blank=True, max_length=100)),
                ('delete_time', models.IntegerField(null=True, blank=True)),
                ('update_time', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'third_app',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('openid', models.CharField(unique=True, max_length=50)),
                ('nickname', models.CharField(null=True, blank=True, max_length=50)),
                ('extend', models.CharField(null=True, blank=True, max_length=255)),
                ('delete_time', models.IntegerField(null=True, blank=True)),
                ('create_time', models.IntegerField(null=True, blank=True)),
                ('update_time', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=20)),
                ('province', models.CharField(null=True, blank=True, max_length=20)),
                ('city', models.CharField(null=True, blank=True, max_length=20)),
                ('country', models.CharField(null=True, blank=True, max_length=20)),
                ('detail', models.CharField(null=True, blank=True, max_length=100)),
                ('delete_time', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField(unique=True)),
                ('update_time', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'user_address',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('product', models.OneToOneField(to='api.Product', serialize=False, primary_key=True, help_text='联合主键，商品id', db_constraint=False)),
                ('count', models.IntegerField(help_text='商品数量')),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('order', models.ForeignKey(to='api.Order', db_constraint=False, help_text='联合主键，订单id')),
            ],
            options={
                'db_table': 'order_product',
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
            },
        ),
        migrations.AddField(
            model_name='theme',
            name='products',
            field=models.ManyToManyField(to='api.Product', related_name='products', db_constraint=False, help_text='商品，多对多关系'),
        ),
        migrations.AddField(
            model_name='theme',
            name='topic_img',
            field=models.OneToOneField(to='api.Image', null=True, blank=True, related_name='topic', db_constraint=False, help_text='图片外键'),
        ),
        migrations.AddField(
            model_name='productproperty',
            name='product',
            field=models.ForeignKey(to='api.Product', db_constraint=False, help_text='商品外键'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(to='api.Product', db_constraint=False, help_text='商品外键'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(to='api.Category', null=True, blank=True, help_text='商品分类外键', db_constraint=False),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ForeignKey(to='api.Image', null=True, blank=True, help_text='图片外键', db_constraint=False),
        ),
        migrations.AddField(
            model_name='category',
            name='topic_img',
            field=models.ForeignKey(to='api.Image', null=True, blank=True, help_text='外键，关联image表', db_constraint=False),
        ),
        migrations.AddField(
            model_name='banneritem',
            name='img',
            field=models.OneToOneField(to='api.Image', help_text='外键，关联image表', db_constraint=False),
        ),
        migrations.AlterUniqueTogether(
            name='orderproduct',
            unique_together=set([('product', 'order')]),
        ),
    ]
