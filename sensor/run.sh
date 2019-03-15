#!/bin/bash

if lsmod | grep "industrialio" &> /dev/null ; then
  echo "industrialio is loaded"
else
  echo "industrialio is not loaded - loading"
	modprobe --first-time industrialio
fi

if lsmod | grep "bme680_core" &> /dev/null ; then
  echo "bme680_core is loaded"
else
  echo "bme680_core is not loaded - loading"
	insmod bme680_core.ko
fi

if lsmod | grep "bme680_i2c" &> /dev/null ; then
  echo "bme680_i2c is loaded"
else
  echo "bme680_i2c is not loaded - loading"
	insmod bme680_i2c.ko
fi

mount -t configfs none /sys/kernel/config
mkdir -p /sys/kernel/config/device-tree/overlays/bme680-breakout
cat bme680-breakout.dtbo > /sys/kernel/config/device-tree/overlays/bme680-breakout/dtbo

echo 8 > /sys/bus/iio/devices/iio\:device0/in_temp_oversampling_ratio
echo 2 > /sys/bus/iio/devices/iio\:device0/in_humidityrelative_oversampling_ratio
echo 4 > /sys/bus/iio/devices/iio\:device0/in_pressure_oversampling_ratio

telegraf
