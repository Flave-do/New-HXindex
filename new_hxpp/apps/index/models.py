from django.db import models
# django自带用户模型下的表
from django.contrib.auth.models import User

# Create your models here.
# 每一个类都必须继承models.Model
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True,)
    # unique 唯一索引 该值不允许重复  该值不允许为空--->blank=False
    username = models.CharField(unique=True,max_length=20,blank=False)


class UserComment(models.Model):
    id = models.AutoField(primary_key=True)
    restore = models.TextField(to='formtexi',to_field='id',verbose_name='客服回复')

    # 联合索引
    class Meta:
        # 唯一联合索引
        unique_together = ['fkauthor','id']
        # # 普通联合索引
        # index_together = ['','']


class FormTexi(models.Model):
    id = models.AutoField(primary_key=True)
    datatimes = models.DateTimeField(verbose_name='时间')
    fkauthor = models.CharField(to='userprofile',to_field='username',max_length=20, blank=False)
    fkwhere = models.CharField(max_length=20, blank=False)
    fkemail = models.EmailField(verbose_name='邮箱')
    fkmotif = models.TextField(verbose_name='标题')
    fkdetails = models.TextField(verbose_name='内容')