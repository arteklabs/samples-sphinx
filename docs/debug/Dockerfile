FROM node:16
WORKDIR /usr/src/app
COPY app.js package.json ./
RUN npm install
ENTRYPOINT [ "node", "app.js" ]
CMD ["8080", "0.0.0.0"]
