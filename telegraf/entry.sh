#!/bin/bash
if [[ -z $INFLUX_TOKEN || -z $INFLUX_ORG || -z $INFLUX_BUCKET ]]; then
  echo 'One or more InfluxDB variables are undefined - not using cloud'
  sed -i '/influxdb_v2/,/bucket/ s/^#*/#/' /etc/telegraf/telegraf.conf
else
  echo 'InfluxDB variables are defined - using cloud'
  sed -i '/influxdb_v2/,/bucket/ s/^##*//' /etc/telegraf/telegraf.conf
fi

telegraf
