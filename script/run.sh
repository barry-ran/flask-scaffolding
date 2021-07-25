docker container stop flask-scaffolding
docker container rm flask-scaffolding
docker image rm flask-scaffolding

docker build -t flask-scaffolding:latest .
docker run -d -p 5000:5000 --name=flask-scaffolding flask-scaffolding
