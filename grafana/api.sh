#!/bin/bash -x

GRAFANA_URL="127.0.0.1:$GF_SERVER_HTTP_PORT"
GRAFANA_DEFAULT_USER="admin"
GRAFANA_DEFAULT_PW="admin"

count=0
max_retries=10

while [[ "$count" < "$max_retries" ]]; do
    if [ "$test_cmd" != 'ok' ]; then
        test_cmd=$(curl "http://$GRAFANA_URL/api/health" | jq -r -e .database)
        count=$(( "$count" + 1 ))
        sleep 10
    fi
    if curl -sq -w "\n" -X PUT "http://$GRAFANA_DEFAULT_USER:$GRAFANA_DEFAULT_PW@$GRAFANA_URL/api/org/preferences" \
        -H 'Accept-Encoding: gzip, deflate, br' -H 'X-Grafana-Org-Id: 1' -H \
            'Content-Type: application/json;charset=UTF-8' -H \ 'Accept: application/json' --data-binary \
                '{"homeDashboardId":1,"theme":"","timezone":""}' --compressed; then
        break
    else
        count=$(( "$count" + 1 ))
    fi
done
