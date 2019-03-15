if [ ! -f /data/grafana/grafana.db ]; then
  mkdir /data/grafana
  cp /tmp/grafana.db /data/grafana/
fi

exec /usr/sbin/grafana-server --homepath /usr/share/grafana
