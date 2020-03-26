'''程序逻辑配置和第三方平台配置'''

from urllib.parse import urlencode

# 七牛云配置
QN_ACCESS_KEY = 'ocRkmfMB3D46b5mYv2x5xo2wtq4sx2QKKZ1e-bKs'
QN_SECRET_KEY = 'REW00si9C53CjBIHa2ufYp0L41pNkYmavEHVPZ0N'
QN_BUCKET = 'xiaobanban'
QN_LOADURL = 'http://q7g6nuyf1.bkt.clouddn.com/'
# 云之讯配置
YZX_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_ARGS = {
    "sid": "6dc8a648e435cd929645f35f42fa3a8f",
    "token": "a9de8f831581733974756177666ddac3",
    "appid": "fdae4294763c4af19b808534f3b2aafa",
    "templateid": "534753",
    "param": None,
    "mobile": None,
}

# 微博配置
WB_APP_KEY = '781700663'
WB_APP_SECRET = '21fcbcf01dd0f54d309125415f8c5c09'
WB_CALLBACK = 'http://127.0.0.1:8000/weibo/callback'
# 第一步: Authorize 接口
#TODO 用户请求授权接口 点击授权 获得code
WB_AUTH_API = 'https://api.weibo.com/oauth2/authorize'
WB_AUTH_ARGS = {
    'client_id': WB_APP_KEY,
    'redirect_uri': WB_CALLBACK,
    'display': 'default'
}
WB_AUTH_URL = '%s?%s' % (WB_AUTH_API, urlencode(WB_AUTH_ARGS))
# 第二步: AccessToken 接口
# TODO 通过code 作为必要的参数 获取用户的access token  和uid
WB_ACCESS_TOKEN_API = 'https://api.weibo.com/oauth2/access_token'
WB_ACCESS_TOKEN_ARGS = {
    'client_id': WB_APP_KEY,
    'client_secret': WB_APP_SECRET,
    'grant_type': 'authorization_code',
    'redirect_uri': WB_CALLBACK,
    'code': None,
}
# 第三步: 获取用户信息
# TODO 获取微博记录的用户信息
WB_USER_SHOW_API = 'https://api.weibo.com/2/users/show.json'
WB_USER_SHOW_ARGS = {
    'access_token': None,
    'uid': None
}
