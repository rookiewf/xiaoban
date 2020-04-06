from django.db import models


# Create your models here.
class Swiper(models.Model):
    STYPE = (
        ('like', '喜欢'),
        ('super_like', '超级喜欢'),
        ('dislike', '不喜欢')
    )
    uid = models.IntegerField(verbose_name='滑动者的id')
    sid = models.IntegerField(verbose_name='被滑者的id')
    stime = models.DateTimeField(auto_now_add=True, verbose_name='滑动时的时刻')
    stype = models.CharField(max_length=12,choices=STYPE, verbose_name='左滑dislike,右滑like,上滑super_like')

    class Meta:
        db_table = 'swiper'

    @classmethod
    def is_liked(cls, uid, sid):
        return cls.objects.filter(
            uid=uid, sid=sid, stype__in=['like', 'super_like']).exists()


class Firend(models.Model):
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    class Meta:
        db_table = 'firend'

    @classmethod
    def make_firends(cls, uid, sid):
        uid1, uid2 = (uid, sid) if uid > sid else (sid, uid)
        cls.objects.create(uid1=uid1,uid2=uid2)