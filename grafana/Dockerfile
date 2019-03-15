FROM balenalib/raspberrypi3

COPY ./grafana.ini /usr/share/grafana/conf/custom.ini
COPY ./grafana.db /tmp

COPY ./start.sh /usr/src/app/start.sh

RUN install_packages \
      fontconfig-config \
      fonts-dejavu-core \
      libfontconfig1 \
      ucf

RUN curl -o /tmp/grafana.deb https://dl.grafana.com/oss/release/grafana_6.0.1_armhf.deb && \
  dpkg -i /tmp/grafana.deb && rm /tmp/grafana.deb

CMD ["/bin/sh","/usr/src/app/start.sh"]
