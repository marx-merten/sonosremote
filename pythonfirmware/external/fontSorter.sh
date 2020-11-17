#!/bin/bash
g=$(grep u8g2_font_ u8g2Fonts/u8g2Fonts.txt | awk -F = '{print $1}'|sort -u)
for f in $g ;do
    grep -B 5 -A 9000 $f u8g2Fonts/u8g2Fonts.txt | grep -m 1 -B 9000 -e "^)"  > t1/$f.txt
done
