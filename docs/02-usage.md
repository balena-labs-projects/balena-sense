# Usage

## Configuration

### Sensor offsets
If required, this project supports offsetting of the measured values before they are recorded in the database.

To offset temperature, add a balenaCloud environment variable called `BALENASENSE_TEMP_OFFSET`, and add an offset in degrees C.

To offset humidity, add a balenaCloud environment variable called `BALENASENSE_HUM_OFFSET` and add a value in % RH.

To adjust the pressure sensor and compensate for altitude, add a balenaCloud environment variable called `BALENASENSE_ALTITUDE` and set it to your altitude above sea level in meters.

### Using 1-wire sensors
To use 1-wire sensors such as the DS18B20 on the Raspberry Pi, you'll need to enable the 1-wire GPIO interface by adding the `w1-gpio` device tree overlay. Information on the 1-wire interface is available at [pinout.xyz](https://pinout.xyz/pinout/1_wire), but in the case of BalenaOS, you can do this easily in the Device Configuration section of the BalenaCloud dashboard by adding a custom configuration variable called `RESIN_HOST_CONFIG_dtoverlay`, with value `w1-gpio`.

More information about device tree overlays and other advanced boot settings for the Raspberry Pi is available in the [BalenaOS docs](https://www.balena.io/docs/reference/OS/advanced/) and [BalenaCloud management reference section](https://www.balena.io/docs/learn/manage/configuration/).

#### Hardware setup

[The Pi Hut guide to using a DS18B20 sensor with a Raspberry Pi](https://thepihut.com/blogs/raspberry-pi-tutorials/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi) shows how to wire these sensors up. Don't forget you'll need a pullup resistor between the Vin and data lines.

#### Multiple 1-wire sensors on one device
1-wire devices each have a unique ID; if you have more than one sensor attached to your Raspberry Pi, it is possible to select which one to use by setting the `BALENASENSE_1WIRE_SENSOR_ID` device variable in BalenaCloud. If no ID is given, the first sensor found will be used.

For more information about how to find the ID for 1-wire devices, the Pi Hut guide referenced above, or [this Raspberry Pi tutorial](https://tutorials-raspberrypi.com/raspberry-pi-temperature-sensor-1wire-ds18b20/) are useful.

### Data outputs
Versions of balenaSense after v1.5 introduce [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) to capture the data from the sensor which permits the feed of data to other sources in addition to the internal InfluxDB instance.