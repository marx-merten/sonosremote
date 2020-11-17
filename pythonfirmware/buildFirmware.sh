curdir=$(pwd)
find . -name "__pycache__" -type d -prune -exec rm -rf '{}' '+'


pushd $HOME/projekteHome/marxworld/electronics/environments/micropython/ports/esp32
export ESPIDF=/Users/stefan/projekteHome/marxworld/electronics/environments/esp32/espidf3
. /Users/stefan/projekteHome/marxworld/electronics/environments/esp32/espidf3/export.sh
export BOARD=GENERIC_SPIRAM
export FLASH_SIZE=16MB
export PORT=/dev/tty.usbserial-AD0KDXKX
export PART_SRC=${curdir}/partitions-remote-py.csv
export FROZEN_MANIFEST=${curdir}/frozenmanifest.py
export PROJECT_DIR=$curdir

echo "building"
make -j8 $*
cp ./build-${BOARD}/firmware.bin ${curdir}/remote-firmware.bin
popd
./checkSizes.sh
