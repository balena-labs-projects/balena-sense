#!/bin/sh

if [ "$1" = "rpi" ]; then
	wget -O /tmp/grafana.deb https://dl.grafana.com/oss/release/grafana-rpi_6.3.6_armhf.deb;
elif [ "$1" = "aarch64" ]; then
	wget -O /tmp/grafana.deb https://dl.grafana.com/oss/release/grafana_6.3.6_arm64.deb;
else
	wget -O /tmp/grafana.deb https://dl.grafana.com/oss/release/grafana_6.3.6_armhf.deb;
fi
