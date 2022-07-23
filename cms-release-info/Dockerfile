FROM registry.access.redhat.com/ubi8/nodejs-14

USER 0
RUN mkdir -p /usr/src/app && \
    chown -R 1001:0 /usr/src/app

USER 1001
WORKDIR /usr/src/app
ADD package* ./
RUN npm ci
ADD . .
CMD ["npm", "start"]
