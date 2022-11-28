---
slug: /

sidebar_position: 1
title: Getting Started
breadcrumbs: false
---

# Getting started

![](https://assets.balena.io/blog-common/2021/07/sensev2.png)

balenaSense is a Raspberry Pi [balenaCloud](https://www.balena.io/cloud/) starter project taking readings from sensors, like a Bosch BME680 or [similar sensors](01-getting-started.md), storing data using InfluxDB and reporting using Grafana. For a detailed, step-by-step build process, please use the official project guide for [balenaSense v2](https://www.balena.io/blog/balenasense-v2-updated-temperature-pressure-and-humidity-monitoring-for-raspberry-pi/).

This project uses the [sensor](https://github.com/balena-labs-projects/sensor), [connector](https://github.com/balena-labs-projects/connector), and [dashboard](https://github.com/balena-labs-projects/dashboard) [balenaBlocks](https://github.com/balena-labs-projects) to reduce the amount of code you need to manage so that you can simply set up your sensor, send data between sensor(s) and database, and immediately access a customizable, remote dashboard.

## Hardware required

![](https://assets.balena.io/blog-common/2021/07/sensev2-daisy.png)

Depending if you’d like to crack out the soldering iron or not will dictate what sensor board you can use; some are plug and play, and some require a little soldering.

- A Raspberry Pi 2Bv1.2/3B/3B+/3A+/4B
- 16GB (or larger) Micro-SD Card (we recommend Sandisk Extreme Pro SD cards)
- [Power supply and cable](https://www.raspberrypi.org/products/raspberry-pi-universal-power-supply/)
- A compatible sensor such as the BME680 and the necessary connectors, see below:

<span id="sensors"></span>

| Sensor Model | Sensor Name                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BME680       | [Bosch Sensortec BME680 sensor](https://www.adafruit.com/product/3660?gclid=CjwKCAjwlrqHBhByEiwAnLmYUA35oSWz41-kN-awvh6RrLW3ar6pT9PYRx2Wjv96wjjn2X8--7JkTxoCk2IQAvD_BwE)                                                                                                                                                                                                                                                                                      |
| BMP180       | [Bosch Sensortec BMP180 sensor](https://www.mouser.com/ProductDetail/Pimoroni/PIM472?qs=P1JMDcb91o7p2TYl00AP7g%3D%3D&mgh=1&gclid=CjwKCAjwlrqHBhByEiwAnLmYUG86Kxt_Xit3Dre0bpv2mnYQayWGvNl3HJkVMq3sZo2dHueu8nEMxBoCdEUQAvD_BwE)                                                                                                                                                                                                                                 |
| BMP280       | [Bosch Sensortec BMP280 sensor](https://www.digikey.com/en/products/detail/bosch-sensortec/BME688/13681287?utm_adgroup=Specialized%20Sensors&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Sensors%2C%20Transducers_NEW&utm_term=&utm_content=Specialized%20Sensors&gclid=CjwKCAjwlrqHBhByEiwAnLmYUJaQDb25oZIKHhtfkN95OBf53m7ppNf2eAb5a_lGi7vB33WQ-wgRshoCR9EQAvD_BwE)                                                                       |
| BME280       | [Bosch Sensortec BME280 sensor](https://www.adafruit.com/product/2652?gclid=CjwKCAjwlrqHBhByEiwAnLmYUD6k6w_hG0mudMCtQOEKALl5MnoLp-Nt2a8LMnyEM9VUgj035BeXiBoCe8sQAvD_BwE)                                                                                                                                                                                                                                                                                      |
| HTU21        | [Measurement Specialties HTU21 humidity & temperature sensor](https://www.adafruit.com/product/1899)                                                                                                                                                                                                                                                                                                                                                          |
| MS8607       | [TE Connectivity PHT sensor](https://www.digikey.com/en/products/detail/te-connectivity-measurement-specialties/SM9236-BCE-S-600-002/14312077?utm_adgroup=Sensors%2C%20Transducers&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Supplier_TE%20Connectivity%20Measurement%20Specialties_0223_Co-op&utm_term=&utm_content=Sensors%2C%20Transducers&gclid=CjwKCAjwlrqHBhByEiwAnLmYUP0rf910QY6zcUkE3w1uyYPi9zdvyV_rb9o_oqFvrJj_4cjLEiBtCBoCG0cQAvD_BwE) |
| VEML6070     | [VEML6070 UV A light sensor](https://www.adafruit.com/product/2899?gclid=CjwKCAjwlrqHBhByEiwAnLmYUFVZUKf4Eh8GjeWTwESBKyvTL73sozbpxi-WuepjSBsUJi0dyBMByBoCcRsQAvD_BwE)                                                                                                                                                                                                                                                                                         |

_Note: we've added a few links to help you shop-- these are not endorsements or affiliated links and are subject to change inventory and availability. Feel free to contribute better links as well._

Many of these sensors now include a simple, solderless connector known as [Stemma QT](https://www.adafruit.com/index.php?main_page=category&cPath=1005) or [SparkFun Qwiic](https://www.sparkfun.com/qwiic). They allow you to daisy-chain multiple connectors together on the same device. If you’re using these types of connectors, you’ll want to get at least one cable [such as this](https://www.adafruit.com/product/4397) that terminates in pin sockets you can connect to the Raspberry Pi.

## Software required

There are multiple ways to deploy the project to your device. Here's a list of software options. You'll find more information about deploying these options later in this doc.

- adding your device to the [balenaSense Open Fleet](https://hub.balena.io/balenalabs/balenasense), where anyone can add a device without a balenaCloud account to try things out
- you can also use the Deploy with balena button below to get started quickly:

[![balenaSense v2 Deploy with balena](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/balena-labs-projects/balena-sense)

_Note: You'll have to set up a balenaCloud account to use this method. balenaCloud starter accounts are free and fully supported up to ten devices._

- if you plan on [cloning this project](https://github.com/balena-labs-projects/balena-sense) and making other changes, you’ll want to [install balenaCLI](https://github.com/balena-io/balena-cli)

Whichever method you choose, you'll want a tool to flash the SD card such as [balenaEtcher](https://www.balena.io/etcher/).

## Hardware setup

All of the supported sensors utilize a two wire serial communications bus called I2C (“eye-squared-see”), simplifying the connections. Along with the two communication wires, there are also two power connectors for a total of four wires. The diagram below shows the typical color codes (in the arrows) for the wires that connect the sensors to the Pi.

![](https://assets.balena.io/blog-common/2021/07/sensev2-pinout.png)

<figure>Source: the [Raspberry Pi Foundation](https://www.raspberrypi.org/documentation/usage/gpio/), modified. </figure>

You may find that the SDA pin is sometimes labelled SDI and the SCL pin is sometimes labelled SCK on certain sensors. You can use these pins if SDA and SCL are not available, as long as the sensor is in the list above and supports I2C. You can daisy chain multiple I2C sensors together, as seen in the image above.

If you make your connections manually, just make sure you only connect similar wires together, such as SDA to SDA and SCL to SCL and so on.

### Automatically sensing sensors

BalenaSense will automatically scan for connected sensors. Each connected I2C sensor has an address that must be unique. This is usually not an issue unless you connect more than one sensor of the same type. If this is the case, check the sensor’s datasheet to see how/if you can change the address of one of the sensors so they don’t conflict. There’s more information about this in the sensor block’s [readme](https://github.com/balena-labs-projects/sensor).

## Deploying the software

You have three options to deploy the software:

### Join our “Open Fleet” for balenaSense

[Becoming part of our Open Fleet](https://hub.balena.io/balenalabs/balenasense) is the fastest option for getting started, as you don’t need to have a balenaCloud account. Follow the directions here to flash an SD card, insert it into your device, and download and run balenaSense. (For more information about using balenaSense, see the “Device first boot” section below)

### Cloning the project (for advanced users)

Advanced users can clone [the project](https://github.com/balena-labs-projects/balena-sense) from GitHub and use the [balena CLI](https://github.com/balena-io/balena-cli) to push the application to their device. This is the best option if you want to tinker with the project and have full control.

Our [Getting Started guide](https://www.balena.io/docs/learn/getting-started/raspberrypi3/python/) covers this option. (Follow the steps below for the third option after you have created an application and pushed the code using the CLI)

### Use Deploy with balena

[Sign up] for a free balenaCloud account (your first ten devices are free and full-featured!) and then use the button below to create and deploy the application:

[![balena deploy button](https://www.balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/balena-labs-projects/balena-sense)

## Setup guides

A full guide covering the initial setup of this project is available on [our blog](https://www.balena.io/blog/balenasense-v2-updated-temperature-pressure-and-humidity-monitoring-for-raspberry-pi/).
