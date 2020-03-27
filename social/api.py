from django.http import JsonResponse
from django.shortcuts import render
from social import logics

# Create your views here.
# 显示推荐好友
from social.models import Swiper


def get_rcmd_users(request):
    users = logics.rcmd_users(request.user)
    # print(users)
    res = [user.to_dict() for user in users]
    return JsonResponse({'code':'1000','data':res})

# 喜欢接口
def like(request):
    # 每滑动一次 产生一个sid
    sid = int(request.POST.get('sid'))
    is_masthed = logics.like_someone(request.user,sid)
    return JsonResponse({'ismathed':is_masthed})