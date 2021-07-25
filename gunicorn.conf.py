import multiprocessing
debug = False
bind = "0.0.0.0:5000"
pidfile = "gunicorn.pid"
workers = multiprocessing.cpu_count()*2 + 1
worker_class = "gevent"
# daemon=True 在docker中不需要daemon运行，反而会导致看不到gunicorn输出而增加排查问题的难度