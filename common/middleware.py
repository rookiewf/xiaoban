from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

from common import stat
from user.models import User


class AuthorizeMiddleware(MiddlewareMixin):
    '''登陆验证中间件'''
    WHITE_LIST = [
        '/api/user/get_vcode',
        '/api/user/check_vcode',
        '/weibo/wb_auth',
        '/weibo/callback',
    ]

    def process_request(self, request):
        if request.path in self.WHITE_LIST:
            return

        uid = request.session.get('uid')
        if not uid:
            return JsonResponse({'code': stat.LOGIN_REQUIRED, 'data': None})
        # 获取当前用户
        request.user = User.objects.get(id=uid)
