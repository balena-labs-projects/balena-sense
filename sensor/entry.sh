#!/bin/bash
mkdir -p /data/sensor
touch /data/sensor/bsec_iaq.state
cp -n /usr/src/app/bsec_bme680_linux/bsec_iaq.config /data/sensor/bsec_iaq.config

python /usr/src/app/scripts/sensor.py
