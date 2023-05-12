FROM python:alpine

RUN apk update \
	&& apk add postgresql-client \
	&& rm -rf /var/lib/apt/lists/* \
  && apk add curl

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY hwproject/ /usr/src/app/
COPY hwproject/hwproject/.env /usr/src/app/
RUN pip install -r requirements.txt 

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
