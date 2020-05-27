# Customization

## Adding support for various sensors
We encourage contributors to add code to extend our supported sensors. Please review [existing issues](https://github.com/balenalabs/balena-sense/issues) to see which sensors and types are currently being worked on. We'll eventually build a list of compatible sensors.

## Feeding to InfluxDB cloud 2.0
Configure the following environment variables within the balenaCloud dashboard to enable the feed to the InfluxDB Cloud 2.0 service:
* `INFLUX_BUCKET` - the name of the bucket you created
* `INFLUX_ORG` - your login email address used for InfluxDB cloud
* `INFLUX_TOKEN` - the read/write token for your bucket

## Feeding to an external InfluxDB instance
Configure the following environment variables within the balenaCloud dashboard to enable a feed to an external InfluxDB instance:
* `INFLUXDB_EXTERNAL_URL` - the HTTP URL to your InfluxDB instance
* `INFLUXDB_EXTERNAL_USERNAME` - the username for authentication to your InfluxDB instance
* `INFLUXDB_EXTERNAL_PASSWORD` - the password for authentication to your InfluxDB instance

## Output to MQTT
Versions of balenaSense after v1.7 have an integrated MQTT broker available on port 1883. You can configure Telegraf to output the sensor data using MQTT by setting the `TELEGRAF_MQTT_URL_PORT` environment variable as follows:
* INTERNAL - Telegraf will send the sensor data to the internal MQTT broker, which other devices on your network can subscribe to and obtain the data
* ip:port - Set to the IP address and port (for instance 192.168.1.100:1883) of an MQTT broker on your network and Telegraf will publish the data to that address (Do not prepend with "mqtt://")
* empty - Set the variable to an empty value or delete it to prevent Telegraf from publishing the sensor data via MQTT (this is the default state)

The MQTT topic will be published in the format balena-sense/(hostname)/balena-sense and the data will be in JSON format. The default hostname is the first seven characters of the unique device UUID, available on the dashboard. Note that if you change the hostname, the topic will still use the first seven characters of the device UUID.

## Multiple sensors
If you're feeding to one of the above services and have multiple sensors, you can add the `BALENASENSE_ID` variable to each of your devices. This will then be passed to the output database along with the measurements, allowing you to filter and plot metrics from each device individually.