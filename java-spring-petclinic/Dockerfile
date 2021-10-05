FROM maven:3.8.2-jdk-11 AS build
COPY src /home/app/src
COPY pom.xml /home/app
RUN mvn package -f /home/app/pom.xml -DskipTests

FROM adoptopenjdk/openjdk8:alpine-slim 
COPY --from=build /home/app/target/spring-petclinic-2.5.0-SNAPSHOT.jar /home/app/spring-petclinic.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/home/app/spring-petclinic.jar"]