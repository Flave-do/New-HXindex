from django.db import models
# django自带用户模型下的表
from django.contrib.auth.models import User

# Create your models here.
# 每一个类都必须继承models.Model
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True,)
    # unique 唯一索引 该值不允许重复  该值不允许为空--->blank=False
    username = models.CharField(unique=True,max_length=20,blank=False)

    def __str__(self):
        # 返回时显示出来的值
        return self.username

class FormTexi(models.Model):
    id = models.AutoField(primary_key=True)
    datatimes = models.DateTimeField(verbose_name='时间')
    fkauthor = models.ForeignKey(to='userprofile',to_field='username',max_length=20, blank=False,on_delete=models.CASCADE)
    fkwhere = models.CharField(max_length=20, blank=False)
    fkemail = models.EmailField(verbose_name='邮箱')
    fkmotif = models.TextField(verbose_name='标题')
    fkdetails = models.TextField(verbose_name='内容')


class UserComment(models.Model):
    id = models.OneToOneField(to='formtexi',to_field='id',primary_key=True,on_delete=models.CASCADE)
    restore = models.TextField(verbose_name='客服回复')
