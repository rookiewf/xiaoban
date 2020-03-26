from user.models import User
import datetime
# 推荐用户
def rcmd_users(user):
    max_birthday = datetime.date.today()-datetime.timedelta(user.profile.max_dating_age*365)
    min_birthday = datetime.date.today()-datetime.timedelta(user.profile.max_dating_age*365)
    print(max_birthday,min_birthday)
    users = User.objects.filter(
        # sex = user.profile.dating_sex,
        # location = user.profile.dating_location,
        birthday__lte = max_birthday,
        birthday__gte = min_birthday

    )[:50]
    return users
