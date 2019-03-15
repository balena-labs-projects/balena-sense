FROM balenalib/raspberrypi3-python

RUN install_packages curl
RUN pip install smbus bme680 influxdb

WORKDIR /usr/src/app

RUN curl -o telegraf.tar.gz https://dl.influxdata.com/telegraf/releases/telegraf-1.10.0_linux_armhf.tar.gz && \
  tar xfzv telegraf.tar.gz && \
  rm telegraf.tar.gz && \
  cp -rl telegraf/* / && \
  rm -rf telegraf

COPY ./scripts ./scripts
RUN chmod +x scripts/*.py

COPY ./telegraf.conf /etc/telegraf/telegraf.conf

CMD telegraf
