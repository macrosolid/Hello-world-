FROM python:latest

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY hwproject/ /usr/src/app/
COPY hwproject/hwproject/.env /usr/src/app/
RUN pip install -r requirements.txt 

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
