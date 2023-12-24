docker build -t app-orchestrating .
docker run -d --name app-orchestrating -p 82:80 app-orchestrating

docker build -t app-orchestrating .
docker tag app-orchestrating:latest fabiojdluz/app-orchestrating:latest
docker push fabiojdluz/app-orchestrating:latest
docker pull fabiojdluz/app-orchestrating:latest
docker run -d --name app-orchestrating -p 83:80 fabiojdluz/app-orchestrating
 