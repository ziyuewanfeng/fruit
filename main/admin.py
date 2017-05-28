# _*_coding:utf-8
from django.contrib import admin

# from models import Question
# Register your models here.
# from models import sell_user,sell_user_fruit,buy_user,com_pass,comment,people_pass
import models

admin.site.register(models.sell_user_fruit)
admin.site.register(models.buy_user)
admin.site.register(models.com_pass)
admin.site.register(models.comment)
admin.site.register(models.people_pass)
admin.site.register(models.sell_user)
# admin.site.register(Question);
