FROM openjdk:10-jdk
LABEL maintainer=dev@dschuldt.de

# system packages
RUN apt update && apt upgrade -y && apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common --no-install-recommends

# docker
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" && \
  apt update && apt install -y docker-ce && curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose 

# nodejs
ADD nodesource.gpg.key /tmp/nodesource.gpg.key
RUN echo 'deb https://deb.nodesource.com/node_8.x sid main' > /etc/apt/sources.list.d/nodesource.list
RUN apt-key add /tmp/nodesource.gpg.key && apt update && apt install -y nodejs

# ansible
RUN apt install -y ansible

# jenkins slave setup
COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY remoting-3.25.jar /usr/share/jenkins/slave.jar
RUN chmod +x /usr/local/bin/jenkins-slave /usr/share/jenkins/slave.jar

ENTRYPOINT ["jenkins-slave"]

