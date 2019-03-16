FROM balenalib/raspberrypi3-python

RUN pip install smbus bme680 influxdb

WORKDIR /usr/src/app

COPY ./scripts ./scripts
RUN chmod +x scripts/*.py

CMD /usr/src/app/scripts/indoor-air-quality.py
