FROM postgres:latest

ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB world
COPY init.sql /docker-entrypoint-initdb.d/
COPY pvdata/ /var/lib/postgresql/data
