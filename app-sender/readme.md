CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


docker build -t app-sender .
docker run -d --name app-sender -p 82:80 app-sender

docker build -t app-sender .
docker tag app-sender:latest fabiojdluz/app-sender:latest
docker push fabiojdluz/app-sender:latest
docker pull fabiojdluz/app-sender:latest
docker run -d --name app-sender -p 82:80 fabiojdluz/app-sender