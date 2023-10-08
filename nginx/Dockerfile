FROM nginx:latest

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

WORKDIR /app

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
