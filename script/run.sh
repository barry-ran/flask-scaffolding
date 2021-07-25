docker container stop flask-scaffolding
docker container rm flask-scaffolding
docker image rm flask-scaffolding

docker build -t flask-scaffolding:latest .
# 不带-d，调试用
#docker run -p 5000:5000 --name=flask-scaffolding flask-scaffolding
docker run -d -p 5000:5000 --name=flask-scaffolding flask-scaffolding
