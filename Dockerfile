# syntax=docker/dockerfile:1
FROM python:3.7-slim-buster

# 设置工作目录(后续都不需要指定完整路径了，默认工作目录/app)
WORKDIR /app

# 复制源码
COPY ./app ./app

# 复制发布相关脚本
COPY requirements.txt requirements.txt
COPY gunicorn.conf.py gunicorn.conf.py

# 安装依赖
RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install gunicorn -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install gevent -i https://pypi.tuna.tsinghua.edu.cn/simple

# 更新apt源
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y nginx supervisor

# 配置nginx
RUN rm /etc/nginx/sites-enabled/default
COPY nginx_flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx_flask.conf /etc/nginx/sites-enabled/nginx_flask.conf
# 是否后台启动：决定启动nginx命令是否block，因为supervisor不能监控后台进程，command 不能为后台运行命令
# 用supervisor启动nginx的话需要关掉daemon
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# 设置环境变量(给flask db用)
ENV FLASK_APP="app:create_app('production')"
ENV FLASK_ENV="production"

# 创建数据库
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# supervisord https://www.jianshu.com/p/0b9054b33db3
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# 运行(最后这条CMD命令需要阻塞，否则docker启动后接着退出)
CMD ["/usr/bin/supervisord"]
