FROM postgres:12.2-alpine

EXPOSE 5432

ENV DB_SERVER=kanban-db
ENV POSTGRES_DB=kanban-db
ENV POSTGRES_USER=kanban
ENV POSTGRES_PASSWORD=kanban