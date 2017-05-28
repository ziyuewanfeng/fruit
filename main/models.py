# _*_ coding:utf-8 _*_
from django.db import models

'''
卖家表中有水果，通过查快递公司，得到快递人员
卖家表有水果
水果评论表中通过卖家id找到水果
'''


# Create your models here.
# 快递员表
class people_pass(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)  # 快递员名字
    sex = models.CharField(max_length=30)  # 性别
    phone_number = models.CharField(max_length=30)  # 电话

    def __unicode__(self):
        return self.name


# 快递公司
class com_pass(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)  # 公司名字
    phone_number = models.CharField(max_length=30)  # 公司服务电话
    address = models.CharField(max_length=100)  # 地址
    people = models.ForeignKey(people_pass)  # 快递员

    def __unicode__(self):
        return self.name


# # 管理员表
# class admin_user(models.Model):
#     id=models.IntegerField(primary_key=id)
#     user_name=models.CharField(max_length=30)
#     password=models.CharField(max_length=30)
#     def __unicode__(self):
#         return self.user_name


# 卖家表
class sell_user(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)  # 姓名
    sex = models.CharField(max_length=30)  # 性别
    user_name = models.CharField(max_length=30)  # 用户名（电话号）
    password = models.CharField(max_length=30)  # 密码
    address = models.CharField(max_length=100)  # 地址
    identity_num = models.CharField(max_length=100)  # 身份证号
    com_pass = models.ForeignKey(com_pass)  # 快递公司

    def __unicode__(self):
        return self.user_name


# 买家表
class buy_user(models.Model):
    # id=models.IntegerField(primary_key=True,db_column='FId')
    name = models.CharField(max_length=30)  # 姓名
    sex = models.CharField(max_length=30)  # 性别
    user_name = models.CharField(max_length=30)  # 用户名（电话号）
    password = models.CharField(max_length=30)  # 密码
    address = models.CharField(max_length=100)  # 地址

    def __unicode__(self):
        return self.user_name


# 水果的评论表
class comment(models.Model):
    # id = models.IntegerField(primary_key=id)
    sell_user = models.ForeignKey(sell_user)  # 卖家
    buy_user = models.ForeignKey(buy_user)  # 买家
    comment = models.CharField(max_length=300)  # 用户评论

    def __unicode__(self):
        return self.comment


# 水果表
class sell_user_fruit(models.Model):
    # id = models.IntegerField(primary_key=id)
    user = models.ForeignKey(sell_user)
    sell_fruit = models.CharField(max_length=200)  # 经营的水果
    picture=models.CharField(max_length=200,default="abt1.jpg") #图片地址
    valuse = models.IntegerField(default=0)  # 价钱

    def __unicode__(self):
        return self.sell_fruit
