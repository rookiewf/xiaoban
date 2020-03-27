from social.models import Swiper, Firend
from user.models import User
import datetime


# 推荐用户
def rcmd_users(user):
    max_birthday = datetime.date.today() - datetime.timedelta(user.profile.max_dating_age * 365)
    min_birthday = datetime.date.today() - datetime.timedelta(user.profile.max_dating_age * 365)
    print(max_birthday, min_birthday)
    users = User.objects.filter(
        # sex = user.profile.dating_sex,
        # location = user.profile.dating_location,
        birthday__lte=max_birthday,
        birthday__gte=min_birthday

    )[:50]
    return users


# 右滑表示喜欢这个人
def like_someone(user, sid):
    # 喜欢则在swiper创建
    Swiper.objects.create(uid=user.id, sid=sid, stype='like')
    # 如果对方也喜欢过自己 则匹配为好友
    if Swiper.is_liked(sid, user.id):
        Firend.make_firends(user.id, sid)
        return True
    else:
        return False
