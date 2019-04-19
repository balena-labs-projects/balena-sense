#!/bin/sh

if [ "$1" = "raspberry-pi" ]; then
	curl -o /tmp/grafana.deb https://dl.grafana.com/oss/release/grafana-rpi_6.1.4_armhf.deb;
else
	curl -o /tmp/grafana.deb https://dl.grafana.com/oss/release/grafana_6.1.4_armhf.deb;
fi
