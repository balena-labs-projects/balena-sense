# openFleets: configure hostname
curl -X PATCH --header "Content-Type:application/json" \
    --data '{"network": {"hostname": "balena"}}' \
    "$BALENA_SUPERVISOR_ADDRESS/v1/device/host-config?apikey=$BALENA_SUPERVISOR_API_KEY"
    
python3 sensor.py
