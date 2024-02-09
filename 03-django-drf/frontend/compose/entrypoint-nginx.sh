#!/usr/bin/env sh

envsubst '\$DJANGO_SERVICE' < /etc/nginx/conf.d/default.conf.tmp > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'
