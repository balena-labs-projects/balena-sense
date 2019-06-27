![](https://balena.io/blog/content/images/2019/03/balenasense-logo.png)
![](https://balena.io/blog/content/images/2019/03/balenaSense_blog.jpg)

A Raspberry Pi [balenaCloud](https://www.balena.io/cloud/) starter project taking readings from a **either a Bosch BME680 sensor or a Sense-HAT**, storing using InfluxDB and reporting using Grafana.

The Bosch BME680 is recommended as it includes sensors for temperature, humidity, pressure and gas content and is available on a breakout board from a few different places for around $10-$20.

As an alternative, if you have one already, you can use the Raspberry Pi Sense-HAT. This however does not include a sensor for gas content and so if you use this the air quality readout is derived from humidity and temperature target values.

The sensor provides a reading for Indoor Air Quality (IAQ) which is a range from 0 to 500 where lower is better, and displays it with a web interface provided by [Grafana](https://github.com/grafana/grafana).

![](https://raw.githubusercontent.com/balena-io-projects/balena-sense/master/images/iaq-ratings.png)

![](https://raw.githubusercontent.com/balena-io-projects/balena-sense/master/images/iaq-screenshot.png)

### Hardware required

![](https://balena.io/blog/content/images/2019/03/hardware-required.jpg)

Here’s the shopping list for this project. Depending if you’d like to crack out the soldering iron or not will dictate what sensor board you can use; some are plug and play, some require a little soldering.

* Raspberry Pi 2Bv1.2/3B/3B+/3A+/Zero
* 8GB (or larger) Micro-SD Card (we recommend Sandisk Extreme Pro SD cards)
* Power supply & micro-USB cable
* Bosch BME680 sensor with breakout board (see below for places to find one) or...
* **Optional:** Sense HAT (optional replacement for the BME680, but does not include an air quality sensor)
* **Optional:** Male-to-female Dupont cables (optional)

You can get hold of the Bosch BME680 sensor on a breakout board from a variety of vendors too, all at varying costs. If you’d like to do everything without a soldering iron, take a look at Pimoroni, who offer a [BME680 breakout board](https://shop.pimoroni.com/products/bme680-breakout) compatible with their [breakout garden HAT](https://shop.pimoroni.com/products/breakout-garden-hat) so that everything plugs together with no soldering required. If you don't want to do any soldering and are happy to sacrifice the air quality reading, you can also use the [Sense HAT](https://shop.pimoroni.com/products/raspberry-pi-sense-hat), with the added bonus that you'll get a smiley face showing on the LED matrix! However, if you're buying hardware specifically for this project, get one of the BME680 options below, don't buy a Sense-HAT just for this!

If you’re happy to do a little soldering, that opens up a few more options:

* [Pimoroni BME680 breakout](https://shop.pimoroni.com/products/bme680-breakout) £18.50
* [Adafruit BME680 breakout](https://www.adafruit.com/product/3660) US$22.50
* [Sparkfun SparkX BME680](https://www.sparkfun.com/products/14570) US$19.95 (can be solder-free with [their HAT](https://www.sparkfun.com/products/14459))
* [Unbranded BME680 breakout](https://www.aliexpress.com/item/BME680-Digital-Temperature-Humidity-Pressure-Sensor-CJMCU-680-High-Altitude-Sensor-Module-Development-Board/32961416338.html) US$9.92


### Software required

We’ve set up this project which contains all of the software, configuration and code you’ll need to start taking readings straight away. We’re going to deploy this project on [balenaCloud](https://www.balena.io/cloud/) using a free account to push the project and all the software to your Raspberry Pi as well as to provide remote access. Therefore, you’ll need:

* Tool to flash your SD card, such as [balenaEtcher](https://www.balena.io/etcher/)
* A [balenaCloud](https://www.balena.io/cloud/) account
* A clone or download of this project


### Configuration

#### Sensor offsets
If required, this project supports offsetting of the measured values before they are recorded in the database.

To offset temperature, add a balenaCloud environment variable called `BALENASENSE_TEMP_OFFSET`, and add an offset in degrees C.

To offset humidity, add a balenaCloud environment variable called `BALENASENSE_HUM_OFFSET` and add a value in % RH.

To adjust the pressure sensor and compensate for altitude, add a balenaCloud environment variable called `BALENASENSE_ALTITUDE` and set it to your altitude above sea level in meters.

#### Data outputs
Versions of balenaSense after v1.5 introduce [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) to capture the data from the sensor which permits the feed of data to other sources in addition to the internal InfluxDB instance.

##### Feeding to InfluxDB cloud 2.0
Configure the following environment variables within the balenaCloud dashboard to enable the feed to the InfluxDB Cloud 2.0 service:
* `INFLUX_BUCKET` - the name of the bucket you created
* `INFLUX_ORG` - your login email address used for InfluxDB cloud
* `INFLUX_TOKEN` - the read/write token for your bucket

##### Feeding to an external InfluxDB instance
Configure the following environment variables within the balenaCloud dashboard to enable a feed to an external InfluxDB instance:
* `INFLUXDB_EXTERNAL_URL` - the HTTP URL to your InfluxDB instance
* `INFLUXDB_EXTERNAL_USERNAME` - the username for authentication to your InfluxDB instance
* `INFLUXDB_EXTERNAL_PASSWORD` - the password for authentication to your InfluxDB instance

##### Multiple sensors
If you're feeding to one of the above services and have multiple sensors, you can add the `BALENASENSE_ID` variable to each of your devices. This will then be passed to the output database along with the measurements, allowing you to filter and plot metrics from each device individually.

### Setup guides
A full guide covering the initial setup of this project is available on [our blog](https://www.balena.io/blog/p/34fa01e1-7c1d-4fba-bb2a-b57c19d13985/).

We published an additional blog covering the setup of a fleet of balenaSense devices to feed to a central database on [our blog here](https://www.balena.io/blog/p/474400e0-e1f7-4c08-b5b3-e993fd12bda9/).
