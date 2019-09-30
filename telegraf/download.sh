#!/bin/sh

if [ "$1" = "aarch64" ]; then
	wget -O /tmp/telegraf.deb https://dl.influxdata.com/telegraf/releases/telegraf_1.12.2-1_arm64.deb
else
	wget -O /tmp/telegraf.deb https://dl.influxdata.com/telegraf/releases/telegraf_1.11.0-1_armhf.deb;
fi
