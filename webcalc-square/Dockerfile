FROM maven:3-jdk-8-alpine

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN mvn package

EXPOSE 80
CMD [ "sh", "-c", "mvn -Dserver.port=80 spring-boot:run" ]
