FROM python:3.8-alpine

RUN apk fix && \
    apk add --no-cache \ 
    tzdata \
    curl
    
ENV TZ=Asia/Jakarta
RUN rm -rf /var/cache/apk/*

RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5001
CMD python producer.py