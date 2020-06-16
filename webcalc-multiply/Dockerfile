FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y golang

COPY . /app
WORKDIR /app/src


#RUN go run App.go
ENTRYPOINT ["go", "run"]

EXPOSE 8080

CMD ["App.go"]
