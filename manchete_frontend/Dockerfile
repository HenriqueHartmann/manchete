FROM node:18-alpine

RUN mkdir -p /app

WORKDIR /app

COPY . /app

RUN yarn

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

CMD [ "yarn", "dev" ]
