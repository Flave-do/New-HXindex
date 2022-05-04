from django import forms
from django.forms import fields
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re


#定义验证规则的函数
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class FkAuth(forms.Form):
    # fields.CharField(initial='python')　　#设置填充表单的默认值
    # ChoiceField字段只能返回字符
    # TypedChoiceField  -- 带有类型转换功能的下拉框

    # fields.CharField(required=False)　　#表单可以为空
    fkauthor = fields.CharField(
        max_length=10,
        label='作者',
    )

    fkwhere = fields.CharField(
        max_length=20,
        label='来自哪',
    )

    # fields.CharField(error_messages={'required': '不能为空', 'invalid': '格式错误'})　 #自定义错误信息
    # fkemail = fields.EmailField(
    #     label='邮箱',
    # )

    fkmotif = fields.CharField(
        label='标题',
    )

    fkdetails = fields.CharField(
        label='内容',

    )


    def clean(self):
        fkauthor = self.cleaned_data.get('fkauthor', '')
        fkwhere = self.cleaned_data.get('fkwhere', '')
        print('1111',fkauthor,fkwhere)


        if len(fkwhere) > 10:
            raise forms.ValidationError('地址名不可超过10个字符')

        if not fkwhere:
            raise forms.ValidationError('地址不可为空')
        
        return self.cleaned_data
        # 把整个clean_data还回去


    # 二次验证函数的名字是固定写法，以clean_开头，后面跟上字段的变量名
    def clean_fkauthor(self):
        fkauthor = self.cleaned_data.get('fkauthor', '')
        if not fkauthor:
            raise forms.ValidationError('用户名不可为空')

        return fkauthor
        # 最后要把数据return回去





























# ------------------------Django Form所有内置字段------------------------
# Field
#     required=True,               是否允许为空
#     widget=None,                 HTML插件
#     label=None,                  用于生成Label标签或显示内容
#     initial=None,                初始值
#     help_text='',                帮助信息(在标签旁边显示)
#     error_messages=None,         错误信息 {'required': '不能为空', 'invalid': '格式错误'}
#     validators=[],               自定义验证规则
#     localize=False,              是否支持本地化
#     disabled=False,              是否可以编辑
#     label_suffix=None            Label内容后缀
#
#
# CharField(Field)
#     max_length=None,             最大长度
#     min_length=None,             最小长度
#     strip=True                   是否移除用户输入空白
#
# IntegerField(Field)
#     max_value=None,              最大值
#     min_value=None,              最小值
#
# FloatField(IntegerField)
#     ...
#
# DecimalField(IntegerField)
#     max_value=None,              最大值
#     min_value=None,              最小值
#     max_digits=None,             总长度
#     decimal_places=None,         小数位长度
#
# BaseTemporalField(Field)
#     input_formats=None          时间格式化
#
# DateField(BaseTemporalField)    格式：2015-09-01
# TimeField(BaseTemporalField)    格式：11:12
# DateTimeField(BaseTemporalField)格式：2015-09-01 11:12
#
# DurationField(Field)            时间间隔：%d %H:%M:%S.%f
#     ...
#
# RegexField(CharField)
#     regex,                      自定制正则表达式
#     max_length=None,            最大长度
#     min_length=None,            最小长度
#     error_message=None,         忽略，错误信息使用 error_messages={'invalid': '...'}
#
# EmailField(CharField)
#     ...
#
# FileField(Field)
#     allow_empty_file=False     是否允许空文件
#
# ImageField(FileField)
#     ...
#     注：需要PIL模块，pip3 install Pillow
#     以上两个字典使用时，需要注意两点：
#         - form表单中 enctype="multipart/form-data"
#         - view函数中 obj = MyForm(request.POST, request.FILES)
#
# URLField(Field)
#     ...
#
#
# BooleanField(Field)
#     ...
#
# NullBooleanField(BooleanField)
#     ...
#
# ChoiceField(Field)
#     ...
#     choices=(),                选项，如：choices = ((0,'上海'),(1,'北京'),)
#     required=True,             是否必填
#     widget=None,               插件，默认select插件
#     label=None,                Label内容
#     initial=None,              初始值
#     help_text='',              帮助提示
#
#
# ModelChoiceField(ChoiceField)
#     ...                        django.forms.models.ModelChoiceField
#     queryset,                  # 查询数据库中的数据
#     empty_label="---------",   # 默认空显示内容
#     to_field_name=None,        # HTML中value的值对应的字段
#     limit_choices_to=None      # ModelForm中对queryset二次筛选
#
# ModelMultipleChoiceField(ModelChoiceField)
#     ...                        django.forms.models.ModelMultipleChoiceField
#
#
#
# TypedChoiceField(ChoiceField)
#     coerce = lambda val: val   对选中的值进行一次转换
#     empty_value= ''            空值的默认值
#
# MultipleChoiceField(ChoiceField)
#     ...
#
# TypedMultipleChoiceField(MultipleChoiceField)
#     coerce = lambda val: val   对选中的每一个值进行一次转换
#     empty_value= ''            空值的默认值
#
# ComboField(Field)
#     fields=()                  使用多个验证，如下：即验证最大长度20，又验证邮箱格式
#                                fields.ComboField(fields=[fields.CharField(max_length=20), fields.EmailField(),])
#
# MultiValueField(Field)
#     PS: 抽象类，子类中可以实现聚合多个字典去匹配一个值，要配合MultiWidget使用
#
# SplitDateTimeField(MultiValueField)
#     input_date_formats=None,   格式列表：['%Y--%m--%d', '%m%d/%Y', '%m/%d/%y']
#     input_time_formats=None    格式列表：['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']
#
# FilePathField(ChoiceField)     文件选项，目录下文件显示在页面中
#     path,                      文件夹路径
#     match=None,                正则匹配
#     recursive=False,           递归下面的文件夹
#     allow_files=True,          允许文件
#     allow_folders=False,       允许文件夹
#     required=True,
#     widget=None,
#     label=None,
#     initial=None,
#     help_text=''
#
# GenericIPAddressField
#     protocol='both',           both,ipv4,ipv6支持的IP格式
#     unpack_ipv4=False          解析ipv4地址，如果是::ffff:192.0.2.1时候，可解析为192.0.2.1， PS：protocol必须为both才能启用
#
# SlugField(CharField)           数字，字母，下划线，减号（连字符）
#     ...
#
# UUIDField(CharField)           uuid类型
