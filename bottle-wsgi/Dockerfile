FROM debian:buster-slim
LABEL maintainer=contact@schuldt.dev

RUN apt update && apt install -y python3 python3-pip python3-setuptools tini --no-install-recommends && \
  pip3 install bottle gunicorn requests && \
  apt autoremove -y && apt clean all -y

COPY *.py /application/
COPY static/ /application/static/
COPY views/ /application/views/

ENTRYPOINT ["tini", "--"]
CMD ["gunicorn","-b","0.0.0.0:80","-w","9","--chdir","/application","app:application"]