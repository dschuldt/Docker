FROM debian:buster-slim
LABEL maintainer=contact@schuldt.dev

COPY tini /tini
RUN apt update && apt install -y python3 python3-pip python3-setuptools --no-install-recommends && \
  pip3 install bottle gunicorn requests && \
  chmod +x /tini

ENTRYPOINT ["/tini", "--"]
