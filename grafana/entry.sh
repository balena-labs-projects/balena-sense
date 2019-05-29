#!/bin/bash
/usr/src/app/api.sh &
grafana-server -homepath /usr/share/grafana
