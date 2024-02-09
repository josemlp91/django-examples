FROM node:12.0.0 as builder

RUN npm install npm@6.9.0
RUN npm install -g @angular/cli@9.1.3

COPY . ./app
WORKDIR /app

RUN npm install
RUN npm update

RUN npm run build-prod

FROM nginx:1-alpine
RUN rm -rf /etc/nginx/conf.d/*
COPY ./compose/prod/nginx.conf.tmp /etc/nginx/conf.d/default.conf.tmp
RUN rm -rf /usr/share/nginx/html/*


COPY ./compose/entrypoint-nginx.sh /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY --from=builder /app/dist/ /usr/share/nginx/html
EXPOSE 80

ENTRYPOINT ["/entrypoint"]


