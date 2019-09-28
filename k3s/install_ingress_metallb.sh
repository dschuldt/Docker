#!/bin/sh

printf "1. install ingress-nginx\n\n"
kubectl apply -f ingress-nginx/01-mandatory.yml
kubectl apply -f ingress-nginx/02-services.yml

printf "\n\n2. install metallb\n\n"
kubectl apply -f metallb/01-metallb.yml
kubectl apply -f metallb/02-configuration.yml

exit 0