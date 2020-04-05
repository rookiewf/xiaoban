from django.db import models

<<<<<<< HEAD

class User(models.Model):
    SEX = (
        ('male', '男性'),
        ('female', '女性')
    )
    LOCATION = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('广州', '广州'),
        ('深圳', '深圳'),
        ('重庆', '重庆'),
        ('西安', '西安'),
        ('武汉', '武汉'),
        ('沈阳', '沈阳'),
    )
    phonenum = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别')
    birthday = models.DateField(default='1990-1-1', verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=20, choices=LOCATION, verbose_name='常居地')
    class Meta:
        db_table = 'user'
    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'sex': self.sex,
            'birthday': str(self.birthday),
            'avatar': self.avatar,
            'location': self.location,
        }


class Profile(models.Model):
    '''交友资料'''
    dating_sex = models.CharField(max_length=8, choices=User.SEX, verbose_name='匹配的性别')
    dating_location = models.CharField(max_length=20, choices=User.LOCATION, verbose_name='目标城市')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=30, verbose_name='最大查找范围')

    vibration = models.BooleanField(default=True, verbose_name='开启震动')
    only_matched = models.BooleanField(default=True, verbose_name='只让匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')
    class Meta:
        db_table = 'profile'
    def to_dict(self):
        return {
            'id': self.id,
            'dating_sex': self.dating_sex,
            'dating_location': self.dating_location,
            'min_dating_age': self.min_dating_age,
            'max_dating_age': self.max_dating_age,
            'min_distance': self.min_distance,
            'max_distance': self.max_distance,
            'vibration': self.vibration,
            'only_matched': self.only_matched,
            'auto_play': self.auto_play,
        }
=======
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
    nickname=  models.CharField(max_length=32,verbose_name='昵称')
    sex=  models.CharField(max_length=8,choices=SEX,verbose_name='性别')
    birthday=  models.DateField(default="1911-1-1",verbose_name='出生年')
    avatar=  models.CharField(max_length=256,verbose_name='个人形象')
    location=  models.CharField(max_length=20,choices=LOCATION,verbose_name='常居地')
    class Meta:
        db_table = 'user'
    def to_dict(self):
        return {
            'ponenum':self.ponenum,
            'nickname':self.nickname,
            'sex':self.sex,
            'birthday':str(self.birthday),
            'avatar':self.avatar,
            'location':self.location,
        }
>>>>>>> 1800c99547ad55952015c78102a95bb7e22f1eda
