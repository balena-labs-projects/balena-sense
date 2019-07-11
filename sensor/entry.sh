#!/bin/bash

# We compare the version of the BSEC library download here
# If it has changed we remove the existing config and state data as they aren't compatible between versions
if ! cmp /usr/src/app/version /data/sensor/version > /dev/null 2>&1
then
  rm -rf /data/sensor
fi

mkdir -p /data/sensor
# As we've now updated, copy the current version here so it matches on next pass
cp /usr/src/app/version /data/sensor/version

touch /data/sensor/bsec_iaq.state
cp -n /usr/src/app/bsec_bme680_linux/bsec_iaq.config /data/sensor/bsec_iaq.config

python /usr/src/app/scripts/sensor.py
