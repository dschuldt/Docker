FROM dschuldt/bottle-wsgi:1.0
LABEL maintainer=contact@schuldt.dev

ADD app.py /app/

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "--chdir", "/app", "app:app"]
