 
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM node:18-alpine

WORKDIR /app

COPY --from=builder /app/dist ./dist

RUN npm install -g server

EXPOSE 8080

RUN cd dist

CMD ["server", "-p 8080"]
