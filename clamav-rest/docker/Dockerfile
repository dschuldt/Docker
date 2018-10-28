FROM python:3.7-alpine
LABEL maintainer=dev@dschuldt.de

COPY app.py /app/
COPY init_clamav.sh /app/
COPY supervisord.conf /etc/supervisor/
COPY clamd.conf /etc/clamav/
COPY crontab /etc/
RUN apk add --no-cache clamav supervisor && \
  pip install bottle gunicorn pyclamd && \
  chmod +x /app/init_clamav.sh

ENTRYPOINT ["supervisord", "--configuration", "/etc/supervisor/supervisord.conf"]
