#!/bin/sh

if [ "$1" = "raspberry-pi" ]; then
	wget -O /tmp/grafana.deb https://dl.grafana.com/oss/release/grafana-rpi_6.2.5_armhf.deb;
else
	wget -O /tmp/grafana.deb https://dl.grafana.com/oss/release/grafana_6.2.5_armhf.deb;
fi
