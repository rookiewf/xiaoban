from multiprocessing import cpu_count

bind = ["127.0.0.1:9000"]
daemon = True  # 守护进程
pidfile = 'logs/guncorn.pid'  # 进程号存储位置

workers = cpu_count() * 2  # 工作进程数量
# guncorn进程中的使用的协程
# worker_class = "gevent" # 指定异步处理的库
worker_class = "egg:meinheld#gunicorn_worker"  # 比gevent更快的异步网络库
worker_connections = 65535  # 单个进程最大连接数

keepalive = 60  # 服务器保持连接的时间，避免频繁的三次握手
timeout = 30  # 每次请求的超时时间
graceful_timeout = 10  # 重启超时时间
forwarded_allow_ips = "*"

# 日志处理
capture_output = True
loglevel = 'info'
errorlog = "logs/error.log"
