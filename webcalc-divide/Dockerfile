FROM ubuntu:18.04

RUN apt-get update -y

Run apt-get install -y python3-pip python3

COPY ./Requirements.txt /app/Requirements.txt

WORKDIR /app

RUN pip3 install -r Requirements.txt

COPY ./src /app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
