FROM maven:3.6.1-jdk-8-slim AS build
WORKDIR /home/app
COPY pom.xml .
COPY src ./src
RUN mvn -f pom.xml clean package -DskipTests

### STAGE 2: Run ###
FROM openjdk:8-alpine
ENV DB_SERVER=kanban-db 
ENV POSTGRES_DB=kanban-db
ENV POSTGRES_USER=kanban
ENV POSTGRES_PASSWORD=kanban

EXPOSE 8080
COPY --from=build /home/app/target/*.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]