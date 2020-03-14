
import requests
from xiaoban import cfg
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