FROM nginx:1.17.0
LABEL maintainer=contact@schuldt.dev

ARG APP_VERSION

RUN echo "<html>This is an application version <strong>${APP_VERSION}</strong></html>" > /usr/share/nginx/html/index.html
