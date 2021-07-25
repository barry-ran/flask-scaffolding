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

# 设置环境变量(给flask db用)
ENV FLASK_APP="app:create_app('production')"
ENV FLASK_ENV="production"

# 创建数据库
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# 运行
CMD [ "gunicorn", "app:create_app('production')", "-c", "gunicorn.conf.py"]
