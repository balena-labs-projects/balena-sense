![balena-sense](https://raw.githubusercontent.com/balena-io-projects/balena-sense/master/images/logo.png)

![](https://balena.io/blog/content/images/2019/03/balenaSense_blog.jpg)

**NOTE: This is the readme for version 2 of balenaSense. See the instructions for earlier versions [here](https://github.com/balenalabs/balena-sense/tree/v1.9.9).**

A Raspberry Pi [balenaCloud](https://www.balena.io/cloud/) starter project that takes readings from a supported sensor (such as the Bosch BME680), stores them using InfluxDB and generates a dashboard using Grafana. The Bosch BME680 is recommended as it includes sensors for temperature, humidity, pressure and gas content and is available on a breakout board from a few different places for around $10-$20. In addition, balenaSense also supports the following sensors:

| Sensor Model | Sensor Name | 
| ------------ | ----------- |
| BME680 | Bosch Sensortec BME680 sensor |
| BMP180 | Bosch Sensortec BMP180 sensor |
| BMP280 | Bosch Sensortec BMP280 sensor |
| BME280 | Bosch Sensortec BME280 sensor |
| HTU21 | Measurement Specialties HTU21 humidity & temperature sensor |
| MS8607 | TE Connectivity PHT sensor | 
| VEML6070 | VEML6070 UV A light sensor |

**The latest version of balenaSense (v2) removes support for 1-wire sensors, Raspberry Pi Sense-HAT, Pimoroni Enviro+ Air Quality and/or indoor air quality readings (IAQ).** See the how it works section below for more details about these changes.

### Hardware required

![](https://github.com/balenalabs/balena-sense/raw/master/images/sense-sensor.jpg)

Here’s the shopping list for this project. Depending if you’d like to crack out the soldering iron or not will dictate what sensor board you can use; some are plug and play, some require a little soldering.

* Raspberry Pi 2Bv1.2/3B/3B+/3A+/4
* 8GB (or larger) Micro-SD Card (we recommend Sandisk Extreme Pro SD cards)
* Power supply & micro-USB cable
* Bosch BME680 sensor with breakout board (see below for places to find one) or a sensor listed above
* **Optional:** Male-to-female Dupont cables (optional)

You can get hold of the Bosch BME680 sensor on a breakout board from a variety of vendors too, all at varying costs. If you’d like to do everything without a soldering iron, take a look at Pimoroni, who offer a [BME680 breakout board](https://shop.pimoroni.com/products/bme680-breakout) compatible with their [breakout garden HAT](https://shop.pimoroni.com/products/breakout-garden-hat) so that everything plugs together with no soldering required. If you don't need the gas sensor readings, the BMP280 is a less expensive alternative.

If you’re happy to do a little soldering, that opens up a few more options:

* [Pimoroni BME680 breakout](https://shop.pimoroni.com/products/bme680-breakout) £18.50
* [Adafruit BME680 breakout](https://www.adafruit.com/product/3660) US$22.50
* [Sparkfun SparkX BME680](https://www.sparkfun.com/products/14570) US$19.95 (can be solder-free with [their HAT](https://www.sparkfun.com/products/14459))
* [Unbranded BME680 breakout](https://www.aliexpress.com/item/BME680-Digital-Temperature-Humidity-Pressure-Sensor-CJMCU-680-High-Altitude-Sensor-Module-Development-Board/32961416338.html) US$9.92


### Software required

Running this project is as simple as deploying it to a balenaCloud fleet.

One-click deploy to balenaCloud:

[![](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy)

### How it works
Version 2 of balenaSense is built using [blocks](https://www.balena.io/blog/introducing-balenablocks-jumpstart-your-iot-app-development/), which are intelligent, drop-in chunks of functionality. This is a major change from earlier versions of balenaSense which used a number of configuration files to tie together the InfluxDB database, Grafana dashboards and sensor readings. Blocks are designed to work together and use auto-discovery (which can be overridden) to pass data amongst themselves.

The task of reading data from the sensors is now handled by our new [sensor block](https://github.com/balenablocks/sensor). Instead of installing separate drivers and using custom code for each type of sensor, the sensor block utilizes Industrial IO (IIO) and relies on the variety of sensor drivers already included in the Linux kernel itself. (You can learn more about the sensor block and its use of IIO in [this recent blog post](https://www.balena.io/blog/balenablocks-in-depth-sensor-and-pulse/).) This means balenaSense now supports a wider variety of sensors as well as multiple connected sensors. 

Currently however, only I2C sensors that are not mounted on a HAT are supported by the sensor block. This means 1-wire sensors, the Raspberry Pi Sense-HAT, and Pimoroni Enviro+ Air Quality HAT are no longer supported by balenaSense. 

The indoor air quality (IAQ) readings in previous versions of balenaSense were dependent on propriatery software that had recurring breaking changes. On multiple occasions, the entire project was broken while new changes were investigated and merged. In addition, to obtain accurate air quality readings on the BME680, specific burn in procedures are required that balenaSense did not support. For these reasons, air quality readings are no longer a part of balenaSense. 

However, blocks are open source and extendable! We're looking into non-proprietary ways to support air quality readings and sensors on HATs. (PRs are welcome!) We believe that this block-based balenaSense is a more flexible solution overall, and a better base for adding more features as time goes on. If there is a feature that you want to see reinstated, please add an issue above.

### Configuration

Each of the blocks that make up balenaSense v2 are customizable through device variables and are summarized below:

##### Sensor

By default, balenaSense transforms the name and values from certain sensors to be more human-readable. For instance, a raw value from a BME680 is `{"temp": 24620.0}` wheras after transformation it is `{"temperature": 24.62}`. You can force the raw values by changing the `RAW_VALUES` device variable to `0` or deleting it. You can also change temperature units by setting the `TEMP_UNIT` variable to `F` for Farenheit or `C` (the default) for Celsius.

You can find all of the sensor block options [here](https://github.com/balenablocks/sensor).

##### Connector
The connector block connects data sources with data sinks using telegraf and code to find other services running on the device. In balenaSense, the data source is the sensor block which publishes sensor readings on it's own HTTP server on port 7575. The data sink is InfluxDB. To override this "wiring" or pull data in from other sources, see the [configuration options](https://github.com/balenablocks/connector#data-sources) for the connector block.

##### Dashboard

The [dashboard block](https://github.com/balenablocks/dashboard) automatically generates Grafana dashboards based on the discovered schema of an InfluxDB instance running on the same device.

### Setup guides
A full guide covering the initial setup of this project, as well as integration with Home Assistant and the use of multiple instances is available on [our blog](https://www.balena.io/blog/balenasense-v2-updated-temperature-pressure-and-humidity-monitoring-for-raspberry-pi/).

### Become a balena poweruser

Want to learn more about what makes balena work? Try one of our [masterclasses](https://www.balena.io/docs/learn/more/masterclasses/overview/). Each lesson is a self-contained, deeply detailed walkthrough on core skills you need to be successful with your next edge project.

Check them out at our [docs](https://www.balena.io/docs/learn/more/masterclasses/overview/). Also, reach out to us on the [Forums](https://forums.balena.io/) if you need help.
