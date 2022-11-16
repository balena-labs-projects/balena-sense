FROM bh.cr/balenalabs/sensor-armv7hf

WORKDIR /usr/src/app

COPY start.sh start.sh

CMD ["bash", "start.sh"]
