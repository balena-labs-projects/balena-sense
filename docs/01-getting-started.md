# Getting started

![](https://raw.githubusercontent.com/balena-io-projects/balena-sense/master/images/iaq-screenshot.png)

balenaSense is a Raspberry Pi [balenaCloud](https://www.balena.io/cloud/) starter project taking readings from a **either a Bosch BME680 sensor, a Sense-HAT, or a 1-wire temperature sensor (such as a Dallas DS18B20)**, storing using InfluxDB and reporting using Grafana. For a detailed, step-by-step build process, please reference these balena blog posts:

* [Basic balenaSense setup](https://www.balena.io/blog/build-an-environment-and-air-quality-monitor-with-raspberry-pi/)
* Setting up [balenaSense with Home Assistant](https://www.balena.io/blog/monitor-air-quality-around-your-home-with-home-assistant-and-balena/)

### A quick note about compatible sensors

The Bosch BME680 is recommended as it includes sensors for temperature, humidity, pressure and gas content and is available on a breakout board from a few different places for around $10-$20.

If you have one already, you can alternatively use the Raspberry Pi Sense-HAT. This, however, **does not include a sensor for gas content** and so if you use this the air quality readout is derived from humidity and temperature target values.

If you have neither a BME680 nor a Sense-HAT, or if you only need temperature readings, you can use a so-called 1-wire sensor, such as the DS18B20. Air quality metrics are not available with these sensors.

![](https://raw.githubusercontent.com/balena-io-projects/balena-sense/master/images/iaq-ratings.png)

The sensor provides a reading for Indoor Air Quality (IAQ) which is a range from 0 to 500 where lower is better, and displays it with a web interface provided by [Grafana](https://github.com/grafana/grafana).

## Hardware required

![](https://balena.io/blog/content/images/2019/03/hardware-required.jpg)

Here’s the shopping list for this project. Depending if you’d like to crack out the soldering iron or not will dictate what sensor board you can use; some are plug and play, and some require a little soldering.

* Raspberry Pi 2Bv1.2/3B/3B+/3A+/Zero/4
* 8GB (or larger) Micro-SD Card (we recommend Sandisk Extreme Pro SD cards)
* Power supply & micro-USB cable
* Bosch BME680 sensor with breakout board (see below for places to find one) or...
* **Optional:** Sense HAT (optional replacement for the BME680, but does not include an air quality sensor)
* **Optional:** 1-wire temperature sensor (temperature only)
* **Optional:** [Pimoroni Enviro+ Air Quality](https://shop.pimoroni.com/products/enviro?variant=31155658457171) (only supports Temp, Humidity, Pressure, Light (Lux), NH3, Oxidising and Reducing Gases currently)
* **Optional:** Male-to-female Dupont cables (optional)

You can get hold of the Bosch BME680 sensor on a breakout board from a variety of vendors too, all at varying costs. If you’d like to do everything without a soldering iron, take a look at Pimoroni, who offer a [BME680 breakout board](https://shop.pimoroni.com/products/bme680-breakout) compatible with their [breakout garden HAT](https://shop.pimoroni.com/products/breakout-garden-hat) so that everything plugs together with no soldering required. If you don't want to do any soldering and are happy to sacrifice the air quality reading, you can also use the [Sense HAT](https://shop.pimoroni.com/products/raspberry-pi-sense-hat), with the added bonus that you'll get a smiley face showing on the LED matrix! However, if you're buying hardware specifically for this project, get one of the BME680 options below, don't buy a Sense-HAT just for this! If you only need temperature readings, you can find DS18B20 1-wire sensors readily available on eBay (and much cheaper than the BME680 or Sense-HAT), with minimal soldering required.

If you’re happy to do a little soldering, that opens up a few more options:

* [Pimoroni BME680 breakout](https://shop.pimoroni.com/products/bme680-breakout) £18.50
* [Adafruit BME680 breakout](https://www.adafruit.com/product/3660) US$22.50
* [Sparkfun SparkX BME680](https://www.sparkfun.com/products/14570) US$19.95 (can be solder-free with [their HAT](https://www.sparkfun.com/products/14459))
* [Unbranded BME680 breakout](https://www.aliexpress.com/item/BME680-Digital-Temperature-Humidity-Pressure-Sensor-CJMCU-680-High-Altitude-Sensor-Module-Development-Board/32961416338.html) US$9.92
* [Dallas DS18B20 1-wire temperature sensor](https://thepihut.com/products/ds18b20-one-wire-digital-temperature-sensor) £4.00 (The Pi Hut also has a [guide to soldering/wiring up these sensors](https://thepihut.com/blogs/raspberry-pi-tutorials/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi), alternatively, DS18B20 sensors in a waterproof casing with flying leads attached are readily available on eBay or similar)

## Software required

### One-click application creation and deploy

You can use the previous steps to deploy this project and learn more about balena CLI. For a faster path, try our one-button deploy. Once you have a balenaCloud account set up, click this button to go straight to application creation, where balenaSense will be pre-loaded to your application:

[![](https://balena.io/deploy.png)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/balenalabs/balena-sense)

## Setup guides
A full guide covering the initial setup of this project is available on [our blog](https://www.balena.io/blog/p/34fa01e1-7c1d-4fba-bb2a-b57c19d13985/).

We published an additional blog covering the setup of a fleet of balenaSense devices to feed to a central database on [our blog here](https://www.balena.io/blog/p/474400e0-e1f7-4c08-b5b3-e993fd12bda9/).