#!/bin/sh

printf "1. install ingress-nginx\n\n"
kubectl apply -f ingress-nginx/mandatory.yml
kubectl apply -f ingress-nginx/service-nodeport.yml

printf "\n\n2. install metallb\n\n"
kubectl apply -f metallb/metallb.yml
kubectl apply -f metallb/configuration.yml

exit 0