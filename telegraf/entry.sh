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

if [[ -z $TELEGRAF_MQTT_URL_PORT ]]; then
  echo 'No Telegraf MQTT URL:Port specified - Telegraf MQTT output disabled'
  sed -i '/MQTTOutput/,/EndMQTTOutput/ s/^#*/#/' /etc/telegraf/telegraf.conf
elif [[ $TELEGRAF_MQTT_URL_PORT == "INTERNAL" ]]; then
  TELEGRAF_MQTT_URL_PORT="mqtt:1883"
  echo 'Internal MQTT server specified for Telegraf - enabling MQTT output to '$TELEGRAF_MQTT_URL_PORT
  sed -i '/MQTTOutput/,/EndMQTTOutput/ { s/^##*//; s/^ MQTTOutput$/# MQTTOutput/; s/^ EndMQTTOutput/# EndMQTTOutput/ }' /etc/telegraf/telegraf.conf
else
  echo 'External MQTT server specified for Telegraf - enabling MQTT output to '$TELEGRAF_MQTT_URL_PORT
  sed -i '/MQTTOutput/,/EndMQTTOutput/ { s/^##*//; s/^ MQTTOutput$/# MQTTOutput/; s/^ EndMQTTOutput/# EndMQTTOutput/ }' /etc/telegraf/telegraf.conf
fi

if [[ $DISABLE_INTERNAL_INFLUXDB == "TRUE" ]]; then
  echo 'Internal InfluxDB disabled'
  sed -i '/InternalInfluxDB/,/EndInternalInfluxDB/ s/^#*/#/' /etc/telegraf/telegraf.conf
else
  echo 'Internal InfluxDB enabled'
  sed -i '/InternalInfluxDB/,/EndInternalInfluxDB/ { s/^##*//; s/^ InternalInfluxDB$/# InternalInfluxDB/; s/^ EndInternalInfluxDB/# EndInternalInfluxDB/ }' /etc/telegraf/telegraf.conf
fi

#Rename this container's hostname
hn=$BALENA_DEVICE_UUID
hp=$(echo $hn | cut -c1-7)
echo 'Changing hostname to '$hp
hostname $hp

exec telegraf
