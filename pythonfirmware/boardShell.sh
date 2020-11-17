#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
port=$(ls -1 /dev/tty.usb*|head -n1)
rshell -l
echo "Choosen $port"
rshell -p ${port} $*