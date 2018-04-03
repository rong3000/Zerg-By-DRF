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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(null=True, blank=True, max_length=50, help_text='Banner名称，通常作为标识')),
                ('description', models.CharField(null=True, blank=True, max_length=255, help_text='Banner描述')),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
            ],
            options={
                'verbose_name_plural': 'Banner',
                'db_table': 'banner',
                'verbose_name': 'Banner',
            },
        ),
        migrations.CreateModel(
            name='BannerItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('key_word', models.CharField(help_text='执行关键字，根据不同的type含义不同', max_length=100)),
                ('type', models.IntegerField(choices=[(0, '无导向'), (1, '导向商品'), (2, '导向专题')], help_text='0:无导向；1：导向商品;2:导向专题', default=1)),
                ('delete_time', models.IntegerField(null=True, blank=True)),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('banner', models.ForeignKey(related_name='items', db_constraint=False, to='api.Banner', help_text='外键，关联banner表')),
            ],
            options={
                'verbose_name_plural': 'Banner子项',
                'db_table': 'banner_item',
                'verbose_name': 'Banner子项',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='分类名称', max_length=50)),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('description', models.CharField(null=True, blank=True, max_length=100, help_text='描述')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
            ],
            options={
                'verbose_name_plural': '商品分类',
                'db_table': 'category',
                'verbose_name': '商品分类',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('url', models.CharField(help_text='图片路径', max_length=255)),
                ('img_from', models.IntegerField(choices=[(1, '本地'), (2, '公网')], help_text='图片来自 1 本地 ，2公网', default=1, db_column='from')),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
            ],
            options={
                'verbose_name_plural': '图片',
                'db_table': 'image',
                'verbose_name': '图片',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('order_no', models.CharField(help_text='订单号', unique=True, max_length=20)),
                ('user_id', models.IntegerField(help_text='外键，用户id，注意并不是openid')),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('create_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('total_price', models.DecimalField(help_text='总价', max_digits=6, decimal_places=2)),
                ('status', models.IntegerField(choices=[(1, '未支付'), (2, '已支付'), (3, '已发货'), (4, '已支付但库存不足')], help_text='1:未支付， 2：已支付，3：已发货 , 4: 已支付，但库存不足', default=1)),
                ('snap_img', models.CharField(null=True, blank=True, max_length=255, help_text='订单快照图片')),
                ('snap_name', models.CharField(null=True, blank=True, max_length=80, help_text='订单快照名称')),
                ('total_count', models.IntegerField(help_text='总数', default=0)),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('snap_items', models.TextField(null=True, blank=True, help_text='订单其他信息快照（json)')),
                ('snap_address', models.CharField(null=True, blank=True, max_length=500, help_text='地址快照')),
                ('prepay_id', models.CharField(null=True, blank=True, max_length=100, help_text='订单微信支付的预订单id（用于发送模板消息')),
            ],
            options={
                'verbose_name_plural': '订单',
                'db_table': 'order',
                'verbose_name': '订单',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='商品名称', max_length=80)),
                ('price', models.DecimalField(help_text='价格,单位：分', max_digits=6, decimal_places=2)),
                ('stock', models.IntegerField(help_text='库存量', default=0)),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('main_img_url', models.CharField(null=True, blank=True, max_length=255, help_text='主图ID号，这是一个反范式设计，有一定的冗余')),
                ('img_from', models.IntegerField(choices=[(1, '本地'), (2, '公网')], help_text='图片来自 1 本地 ，2公网', db_column='from')),
                ('create_time', models.IntegerField(null=True, blank=True, help_text='创建时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('summary', models.CharField(null=True, blank=True, max_length=50, help_text='摘要')),
            ],
            options={
                'verbose_name_plural': '商品',
                'db_table': 'product',
                'verbose_name': '商品',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('order', models.IntegerField(help_text='图片排序序号')),
                ('img', models.OneToOneField(db_constraint=False, to='api.Image', help_text='图片外键')),
            ],
            options={
                'verbose_name_plural': '商品图片',
                'db_table': 'product_image',
                'verbose_name': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(null=True, blank=True, max_length=30, help_text='详情属性名称')),
                ('detail', models.CharField(help_text='详情属性', max_length=255)),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
            ],
            options={
                'verbose_name_plural': '商品属性',
                'db_table': 'product_property',
                'verbose_name': '商品属性',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(null=True, blank=True, max_length=255)),
                ('delete_time', models.IntegerField(null=True, blank=True)),
                ('update_time', models.IntegerField(null=True, blank=True)),
                ('head_img', models.OneToOneField(related_name='head', help_text='图片外键', to='api.Image', null=True, blank=True, db_constraint=False)),
            ],
            options={
                'db_table': 'theme',
            },
        ),
        migrations.CreateModel(
            name='ThirdApp',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('openid', models.CharField(help_text='wechat openid', unique=True, max_length=50)),
                ('nickname', models.CharField(null=True, blank=True, max_length=50, help_text='昵称')),
                ('extend', models.CharField(null=True, blank=True, max_length=255)),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('create_time', models.IntegerField(null=True, blank=True, help_text='创建时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='姓名', max_length=30)),
                ('mobile', models.CharField(help_text='手机号', max_length=20)),
                ('province', models.CharField(null=True, blank=True, max_length=20, help_text='省')),
                ('city', models.CharField(null=True, blank=True, max_length=20, help_text='城市')),
                ('country', models.CharField(null=True, blank=True, max_length=20, help_text='国家')),
                ('detail', models.CharField(null=True, blank=True, max_length=100, help_text='详情')),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('user', models.OneToOneField(related_name='address', help_text='用户', to='api.User', null=True, blank=True, db_constraint=False)),
            ],
            options={
                'db_table': 'user_address',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('product', models.OneToOneField(serialize=False, to='api.Product', help_text='联合主键，商品id', primary_key=True, db_constraint=False)),
                ('count', models.IntegerField(help_text='商品数量')),
                ('delete_time', models.IntegerField(null=True, blank=True, help_text='删除时间')),
                ('update_time', models.IntegerField(null=True, blank=True, help_text='更新时间')),
                ('order', models.ForeignKey(to='api.Order', help_text='联合主键，订单id', db_constraint=False)),
            ],
            options={
                'verbose_name_plural': '订单商品',
                'db_table': 'order_product',
                'verbose_name': '订单商品',
            },
        ),
        migrations.AddField(
            model_name='theme',
            name='product',
            field=models.ManyToManyField(to='api.Product', help_text='商品，多对多关系', related_name='products', db_constraint=False),
        ),
        migrations.AddField(
            model_name='theme',
            name='topic_img',
            field=models.OneToOneField(related_name='topic', help_text='图片外键', to='api.Image', null=True, blank=True, db_constraint=False),
        ),
        migrations.AddField(
            model_name='productproperty',
            name='product',
            field=models.ForeignKey(related_name='properties', db_constraint=False, to='api.Product', help_text='商品外键'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(related_name='images', db_constraint=False, to='api.Product', help_text='商品外键'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(help_text='商品分类外键', to='api.Category', null=True, blank=True, db_constraint=False),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.OneToOneField(help_text='图片外键', to='api.Image', null=True, blank=True, db_constraint=False),
        ),
        migrations.AddField(
            model_name='category',
            name='topic_img',
            field=models.OneToOneField(help_text='外键，关联image表', to='api.Image', null=True, blank=True, db_constraint=False),
        ),
        migrations.AddField(
            model_name='banneritem',
            name='img',
            field=models.OneToOneField(db_constraint=False, to='api.Image', help_text='外键，关联image表'),
        ),
        migrations.AlterUniqueTogether(
            name='orderproduct',
            unique_together=set([('product', 'order')]),
        ),
    ]
