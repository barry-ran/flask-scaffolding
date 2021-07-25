# syntax=docker/dockerfile:1
FROM python:3.7-slim-buster

# 设置工作目录(后续都不需要指定完整路径了，默认工作目录/app)
WORKDIR /app

# 复制源码
COPY ./app ./app

# 复制发布相关脚本
COPY requirements.txt requirements.txt

# 安装依赖
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 设置环境变量
ENV FLASK_APP="app:create_app('production')"
ENV FLASK_ENV="production"

# 运行
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
