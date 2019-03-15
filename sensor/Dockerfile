FROM balenalib/raspberrypi3:build AS build

RUN install_packages libelf-dev awscli

COPY . /usr/src/app
WORKDIR /usr/src/app

ENV VERSION '2.29.2+rev2.prod'

RUN chmod +x build.sh

RUN ./build.sh raspberrypi3 $VERSION bme680_i2c

RUN curl -o telegraf.tar.gz https://dl.influxdata.com/telegraf/releases/telegraf-1.10.0_linux_armhf.tar.gz

FROM balenalib/raspberrypi3-python

WORKDIR /usr/src/app

COPY --from=build /usr/src/app/compiled ./
COPY --from=build /usr/src/app/telegraf.tar.gz ./
COPY ./bme680-breakout.dtbo ./
COPY ./run.sh ./

RUN chmod +x run.sh

RUN tar xfzv telegraf.tar.gz && \
  rm telegraf.tar.gz && \
  cp -rl telegraf/* / && \
  rm -rf telegraf

COPY ./airquality.py ./
RUN chmod +x airquality.py
COPY ./telegraf.conf /etc/telegraf/telegraf.conf

CMD ./run.sh
