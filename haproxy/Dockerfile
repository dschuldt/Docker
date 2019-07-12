FROM haproxy:2.0.1
LABEL maintainer=contact@schuldt.dev

COPY haproxy.cfg /etc/haproxy/
COPY example.org.pem /etc/ssl/

STOPSIGNAL SIGUSR1
ENTRYPOINT [""]
CMD ["haproxy", "-W", "-db", "-f", "/etc/haproxy/haproxy.cfg"]