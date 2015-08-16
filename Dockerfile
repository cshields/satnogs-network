FROM python2.7
RUN apt-get install libjpeg-turbo8-dev libxml2-dev libxslt1-dev mysql-client \
                    libmysqlclient-dev git gcc

COPY ./requirements/ /tmp/requirements/
RUN pip install -r /tmp/requirements/docker.txt

WORKDIR /app
COPY . /app

EXPOSE 80

CMD ["./docker/run-docker.sh"]
