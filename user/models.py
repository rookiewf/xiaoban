from django.db import models

# Create your models here.
class User(models.Model):
    SEX = (
        ('male','男性'),
        ('female','女性')
    )
    LOCATION = (
        ('北京市','北京市'),('上海市','上海市'),('天津市','天津市'),('重庆市','重庆市'),('河北省','河北省'),
        ('山西省','山西省'),('辽宁省','辽宁省'),('吉林省','吉林省'),('黑龙江省','黑龙江省'),('江苏省','江苏省'),
        ('浙江省','浙江省'),('安徽省','安徽省'),('福建省','福建省'),('江西省','江西省'),('山东省','山东省'),('河南省','河南省'),
        ('湖北省','湖北省'),('湖南省','湖南省'),('广东省','广东省'),('海南省','海南省'),('四川省','四川省'),('贵州省','贵州省'),
        ('云南省','云南省'),('陕西省','陕西省'),('甘肃省','甘肃省'),('青海省','青海省'),('台湾省','台湾省')
    )
    ponenum=  models.CharField(max_length=32,unique=True,verbose_name='手机号')
    nickname=  models.CharField(max_length=32,unique=True,verbose_name='昵称')
    sex=  models.CharField(max_length=8,choices=SEX,verbose_name='性别')
    birthday=  models.DateField(default="1911-1-1",verbose_name='出生年')
    avatar=  models.CharField(max_length=256,verbose_name='个人形象')
    location=  models.CharField(max_length=20,choices=LOCATION,verbose_name='常居地')
    class Meta:
        db_table = 'user'