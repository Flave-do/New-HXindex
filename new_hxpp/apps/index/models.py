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
    fkauthor = models.ForeignKey(to='userprofile',to_field='username', on_delete=models.CASCADE)
    datatime = models.DateTimeField(verbose_name='时间')
    motif = models.TextField(verbose_name='标题')
    details = models.TextField(verbose_name='内容')
    restore = models.TextField(verbose_name='客服')

    # 联合索引
    class Meta:
        # 唯一联合索引
        unique_together = ['fkauthor','id']
        # # 普通联合索引
        # index_together = ['','']
