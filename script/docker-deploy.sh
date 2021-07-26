docker container stop flask-scaffolding
docker container rm flask-scaffolding
docker image rm flask-scaffolding

docker build -t flask-scaffolding:latest .
# 调试用：前台运行
#docker run -p 5000:80 --name=flask-scaffolding -v $(pwd)/app:/deploy/app flask-scaffolding
# 调试用：后台运行并且不退出
#docker run -dit -p 5000:80 --name=flask-scaffolding -v $(pwd)/app:/deploy/app flask-scaffolding
docker run -d -p 5000:80 --name=flask-scaffolding -v $(pwd)/app:/deploy/app flask-scaffolding
