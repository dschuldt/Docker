#!/bin/sh

printf "1. check cluster\n\n"
linkerd check --pre

printf "\n\n2. install linkerd\n\n"
linkerd install | kubectl apply -f -
kubectl apply -f linkerd

exit 0
