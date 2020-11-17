#!/bin/bash
appSize=$(ls -l ../../../environments/micropython/ports/esp32/build-GENERIC_SPIRAM/application.bin | awk  '{print $5}')
otaHex=$(grep ota_0 partitions-remote-py.csv| awk -F , '{print $5}'| awk -F x '{print $2}')


echo "Application Size     $appSize"

otaDec=$((16#$otaHex))
echo "Flash Partition Size $otaDec"
echo "Available            $(bc <<< "scale=2; ${otaDec}-${appSize}")"
percentage=$(bc <<< "scale=2; ${appSize}*100/${otaDec}")
echo "Used $percentage %"
