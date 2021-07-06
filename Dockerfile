FROM balenablocks/sensor

WORKDIR /usr/src/app

COPY start.sh start.sh

CMD ["bash", "start.sh"]
