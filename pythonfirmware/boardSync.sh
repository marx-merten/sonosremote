#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
${DIR}/boardShell.sh rsync -m  $DIR/pysrc/live /pyboard
