import scripts
import random
import datetime
from multiprocessing import Process
from user.models import User
first_name = (
        '赵钱孙李周吴郑王'
        '冯陈褚卫蒋沈韩杨'
        '朱秦尤许何吕施张'
        '孔曹严华金魏陶姜'
        '戚谢邹喻柏水窦章'
        '云苏潘葛奚范彭郎'
        '鲁韦昌马苗凤花方'
        '俞任袁柳酆鲍史唐'
        '费廉岑薛雷贺倪汤'
)
second_name = (
                '寒夜' , '寒月' , '清寒' , '听雨' , '玄冥' , '轩逸',
                '宣城' , '宵狼' , '铭泽' , '铭洋' , '铭浩' , '铭阳',
                '明念' , '念兮' , '玖兮' , '玖舞' , '麟语' , '麟羽',
                '逸景' , '逸风' , '语萱' , '晨曦' , '晨阳' , '辰溪',
                '花诚' , '芊羽' , '芊墨' , '芊芊' , '阡陌' , '浅蒂',
                '陌离' , '倩茹' , '倩怡' , '昔阳' , '戏志' , '心勇',
                '寒云' , '冰旋' , '宛儿' , '盼儿' , '晓霜' , '平安',
                '碧凡' , '夏菡' , '曼香' , '若烟' , '半梦' , '雅绿',
                '翠风' , '香巧' , '代云' , '友巧' , '听寒' , '梦柏',
                '怀亦' , '笑蓝' , '春翠' , '靖柏' , '书雪' , '冰蓝',
                '乐枫' , '念薇' , '靖雁' , '寻春' , '恨山' , '从寒',
                '觅波' , '静曼' , '凡旋' , '千琴' , '恨天' , '醉易',
                '代真' , '新蕾' , '雁玉' , '冷卉' , '紫山' , '忆香',
                '傲芙' , '盼山' , '怀蝶' , '半芹' , '如霜' , '谷雪',
                '冰兰' , '问旋' , '从南' , '白易' , '问筠' , '怜云',

)

def set_name(n):
    for i in range(n):
        year = random.randint(1970,2002)
        month = random.randint(1,12)
        day = random.randint(1,28)
        birthday = datetime.date(year,month,day)
        name = random.choice(first_name) + random.choice(second_name)
        sex = random.choice(User.SEX)[0]
        phonenum = str(random.randrange(20000000000,29999999999,1))
        location = random.choice(User.LOCATION)[0]
        User.objects.create(
            nickname = name,
            phonenum = phonenum,
            sex = sex,
            birthday = birthday,
            location = location
        )

        print(i,name,birthday,sex,location)

if __name__ == '__main__':
    start_time = datetime.datetime.today()
    for i in range(20):
        p = Process(target=set_name,args=(50000,))
        p.start()
        # set_name(10000)
    end_time = datetime.datetime.today()
    use_time = (end_time-start_time).seconds
    print(f'使用了{use_time}s')
#TODO 不使用进程 1*10**4  用了73s完成
# TODO 使用 10 进程 用了20s  100~ 18s  20 ~ 14s
