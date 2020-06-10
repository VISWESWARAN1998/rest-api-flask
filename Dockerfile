# SWAMI KARUPPASWAMI THUNNAI

FROM centos:8

MAINTAINER VISWESWARAN NAGASIVAM (visweswaran.nagasivam98@gmail.com)

RUN yum install gcc python3 python3-devel -y

RUN pip3 install flask flask-restful pyjwt pymysql py-bcrypt

WORKDIR /app

COPY . /app

CMD ["python3", "rest.py"]

