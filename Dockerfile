FROM node:20.8.1 AS build
ENV DOCKER_DEFAULT_PLATFORM=linux/amd64
WORKDIR /usr/app
COPY . /usr/app
RUN npm install
RUN npm run build


FROM nginx:1.25.2-alpine-slim
COPY --from=build /usr/app/build /usr/share/nginx/html
EXPOSE 80