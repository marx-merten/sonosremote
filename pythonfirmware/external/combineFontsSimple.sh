#/!bin/bash
find ./t1 -name "u8g2_font_${1}*.txt" -exec cat "{}" ";" >> u8g2Fonts/${1}.py
find ./t1 -name "u8g2_font_${1}*.txt" -exec rm -f "{}" ";"
