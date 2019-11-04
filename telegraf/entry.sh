#!/bin/bash
if [[ -z $INFLUX_TOKEN || -z $INFLUX_ORG || -z $INFLUX_BUCKET ]]; then
  echo 'One or more InfluxDB Cloud variables are undefined - cloud disabled'
  sed -i '/InfluxDBCloud/,/EndInfluxDBCloud/ s/^#*/#/' /etc/telegraf/telegraf.conf
else
  echo 'InfluxDB variables are defined - cloud enabled'
  sed -i '/InfluxDBCloud/,/EndInfluxDBCloud/ { s/^##*//; s/^ InfluxDBCloud$/# InfluxDBCloud/; s/^ EndInfluxDBCloud/# EndInfluxDBCloud/ }' /etc/telegraf/telegraf.conf
fi

if [[ -z $INFLUXDB_EXTERNAL_URL || -z $INFLUXDB_EXTERNAL_USERNAME || -z $INFLUXDB_EXTERNAL_PASSWORD ]]; then
  echo 'One or more External InfluxDB variables are undefined - external DB disabled'
  sed -i '/ExternalInfluxDB/,/EndExternalInfluxDB/ s/^#*/#/' /etc/telegraf/telegraf.conf
else
  echo 'External InfluxDB variables are defined - external DB enabled'
  sed -i '/ExternalInfluxDB/,/EndExternalInfluxDB/ { s/^##*//; s/^ ExternalInfluxDB$/# ExternalInfluxDB/; s/^ EndExternalInfluxDB/# EndExternalInfluxDB/ }' /etc/telegraf/telegraf.conf
fi

if [[ $DISABLE_INTERNAL_INFLUXDB == "TRUE" ]]; then
  echo 'Internal InfluxDB disabled'
  sed -i '/InternalInfluxDB/,/EndInternalInfluxDB/ s/^#*/#/' /etc/telegraf/telegraf.conf
else
  echo 'Internal InfluxDB enabled'
  sed -i '/InternalInfluxDB/,/EndInternalInfluxDB/ { s/^##*//; s/^ InternalInfluxDB$/# InternalInfluxDB/; s/^ EndInternalInfluxDB/# EndInternalInfluxDB/ }' /etc/telegraf/telegraf.conf
fi

telegraf
