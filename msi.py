
import requests
from django.core.cache import cache

import cfg
import random

def get_vcode(length):
    """ 生成指定长度的验证码 """
    # chars = [str(random.randint(0,9)) for i in range(length)]
    # print(''.join(chars))
    # return ''.join(chars)
    code = []
    for i in range(length):
        code.append(str(random.randint(0,9)))
    # print(''.join(code))
    return ''.join(code)

def send_code(ponenum):
    YZX_CFG = cfg.YZX_CFG.copy()
    vcode = get_vcode(5)
    cache.set('v_code-%s'%ponenum,vcode,120)
    YZX_CFG['mobile'] = ponenum
    YZX_CFG['param'] = vcode
    response = requests.post(url=cfg.YZX_API,json=YZX_CFG)
    if response.status_code == 200:
        result= response.json()
        # print(result)
        if result['code'] == '105140':
            print('验证码:%s'%vcode)
            return True
        return False
send_code('17621463629')