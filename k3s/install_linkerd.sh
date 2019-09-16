#!/bin/sh

printf "1. check cluster\n\n"
linkerd check --pre

printf "\n\n2. install linkerd\n\n"
linkerd install | kubectl apply -f -

exit 0
