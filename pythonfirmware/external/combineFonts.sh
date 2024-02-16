#/!bin/bash
find ./t1 -name "${1}*.txt" -exec cat "{}" ";" >> $2
find ./t1 -name "${1}*.txt" -exec rm -f "{}" ";"
