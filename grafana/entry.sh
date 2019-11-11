#!/bin/bash
/usr/src/app/api.sh &
exec grafana-server -homepath /usr/share/grafana
