# ClamAV API
A simple webservice, build with the amazing [Bottle Framework](https://bottlepy.org) and reliable [ClamAV](https://www.clamav.net/) antivirus scan engine. 

# Setup

    docker run --name clamav-rest -d -p 80:80 dschuldt/clamav-rest 
Or build an Image yourself; Dockerfile is included in "Docker" directory.

The startup duration depends on several factors. Please consider [How does it work](#how) for more information.

# Usage
## Endpoints
### Info
\<docker-url>/info:
- if ClamAV daemon is ready, returns status 200 and content like 

> ClamAV version ClamAV 0.100.1/25069/Fri Oct 26 18:58:31 2018
- if not yet ready, returns status 503 and content
> ClamAV daemon is not ready to accept requests

### Scan
\<docker-url>/scan:

Send a POST request with a Content-Type multipart/form-data file named "data".
E.g. with Curl: 

> curl -F 'data=@examples/normal.file' \<docker-url>/scan

- if ClamAV daemon is not ready, returns status 503 and content 
> ClamAV daemon is not ready to accept requests
- if a virus is found, returns status 200 and content like
> ('FOUND', 'Eicar-Test-Signature')
- if no virus is found, returns status 204 and no content


## <a name="how"></a> How does it work 

After starting the container, [Supervisord](http://supervisord.org/) starts several processes:

- init-clamav: Checks if a clamav database is present and starts the clamd with supervisorctl. If no database is present, freshclam is run beforehand
- clamav-api: This is the Bottle application, run in [Gunicorn](https://gunicorn.org/) WSGI HTTP Server
- crond: the cron daemon, running freshclam every 30 minutes to update the virus database in background

If no virus database is found at startup time, freshclam is run. During the update, clamd is unavailable so the api server will respond with a 503 status. Depending on your setup/ internet connection this process can take some time. Check /info endpoint periodically for readiness probes.
Use a volume mount  (see docker-compose.yml in Docker directory) to persist the database.
If behind a http proxy, mount a freshclam.conf with proper setup in /etc/clamav/.
