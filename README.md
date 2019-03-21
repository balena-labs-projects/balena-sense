# balenaSense

A Raspberry Pi [balenaCloud](https://www.balena.io/cloud/) starter project taking readings from a **either a Bosch BME680 sensor or a Sense-HAT**, storing using InfluxDB and reporting using Grafana.

The Bosch BME680 is recommended as it includes sensors for temperature, humidity, pressure and gas content and is available on a breakout board from a few different places for around $10-$20.

As an alternative, if you have one already, you can use the Raspberry Pi Sense-HAT. This however does not include a sensor for gas content and so if you use this the air quality readout is derived from humidity and temperature target values.
