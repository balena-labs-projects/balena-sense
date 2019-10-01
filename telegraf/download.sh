#!/bin/sh

outfile="/tmp/telegraf.deb"
download_base="https://dl.influxdata.com/telegraf/releases/"
case $1 in
   aarch64) package_file="telegraf_1.12.2-1_arm64.deb"
       ;;
    *) package_file="telegraf_1.12.2-1_armhf.deb"
esac
wget -O "${outfile}" "${download_base}${package_file}"
