![](https://balena.io/blog/content/images/2019/03/balenasense-logo.png)
![](https://balena.io/blog/content/images/2019/03/balenaSense_blog.jpg)

A Raspberry Pi [balenaCloud](https://www.balena.io/cloud/) starter project taking readings from a **either a Bosch BME680 sensor or a Sense-HAT**, storing using InfluxDB and reporting using Grafana.

The Bosch BME680 is recommended as it includes sensors for temperature, humidity, pressure and gas content and is available on a breakout board from a few different places for around $10-$20.

As an alternative, if you have one already, you can use the Raspberry Pi Sense-HAT. This however does not include a sensor for gas content and so if you use this the air quality readout is derived from humidity and temperature target values.

### Hardware required

Here’s the shopping list for this project. Depending if you’d like to crack out the soldering iron or not will dictate what sensor board you can use; some are plug and play, some require a little soldering.

* Raspberry Pi 2Bv1.2/3B/3B+/3A+/Zero
* 8GB (or larger) Micro-SD Card (we recommend Sandisk Extreme Pro SD cards)
* Power supply & micro-USB cable
* Bosch BME680 sensor with breakout board (see below for places to find one) or...
* **Optional:** Sense HAT (optional replacement for the BME680, but does not include an air quality sensor)
* **Optional:** Male-to-female Dupont cables (optional)

You can get hold of the Bosch BME680 sensor on a breakout board from a variety of vendors too, all at varying costs. If you’d like to do everything without a soldering iron, take a look at Pimoroni, who offer a [BME680 breakout board](https://shop.pimoroni.com/products/bme680-breakout) compatible with their [breakout garden HAT](https://shop.pimoroni.com/products/breakout-garden-hat) so that everything plugs together with no soldering required. If you don't want to do any soldering and are happy to sacrifice the air quality reading, you can also use the [Sense HAT](https://shop.pimoroni.com/products/raspberry-pi-sense-hat), with the added bonus that you'll get a smiley face showing on the LED matrix!

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

### A full guide to setting up this project is available on [our blog](https://www.balena.io/blog/p/34fa01e1-7c1d-4fba-bb2a-b57c19d13985/).

