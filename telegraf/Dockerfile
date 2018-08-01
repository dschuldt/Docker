FROM debian:stretch-slim
LABEL maintainer=dev@dschuldt.de

ADD https://github.com/krallin/tini/releases/download/v0.18.0/tini /tini

RUN apt update && apt install -y curl gnupg2 apt-transport-https && \
  curl -sL https://repos.influxdata.com/influxdb.key | apt-key add - && \
  echo "deb https://repos.influxdata.com/debian stretch stable" > /etc/apt/sources.list.d/influxdb.list && \
  apt update && apt install -y telegraf && \
  chmod +x /tini

ENTRYPOINT ["/tini", "--"]
CMD ["telegraf","--config", "/telegraf.conf"]