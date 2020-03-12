
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
import msi
# Create your views here.
from user.models import User

def send_vcode(request):
    ponenum = request.GET.get('ponenum')
    if msi.send_code(ponenum):
        return JsonResponse({"code":"0000","data":"发送成功"})
    else:
        return JsonResponse({"code":"1000","data":"发送失败"})
# 检查验证码，并登录注册
def check_code(request):
    ponenum = request.POST.get('ponenum')
    vcode = request.POST.get('vcode')
    cache_code = cache.get('v_code-%s'%ponenum)
    # 验证验证码
    if vcode and cache_code and cache_code == vcode:
        try:
            user = User.objects.get(ponenum=ponenum)
        except User.DoesNotExist:
            user = User.objects.create(
                ponenum = ponenum,
                nickname = ponenum
            )
            print(user)
        request.session['user_id'] = user.id
        return JsonResponse({"code":'1000',"data":user.to_dict()})
    else:
        return JsonResponse({"code":'10001',"data":"验证码不正确或验证码失效"})
