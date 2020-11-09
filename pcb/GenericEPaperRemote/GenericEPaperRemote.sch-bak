EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Sheet
S 900  800  1550 1400
U 5F59A539
F0 "Connectors" 50
F1 "connectors.sch" 50
F2 "EN" I R 2450 1200 50 
F3 "IO0" I R 2450 1300 50 
F4 "ESP_RX" I R 2450 1700 50 
F5 "ESP_TX" I R 2450 1800 50 
$EndSheet
Text Notes 950  1000 0    50   ~ 0
All inbound connectors (USB, UART), \ntestpoints and power supply
$Comp
L power:+3.3V #PWR07
U 1 1 5F6E3C3B
P 8450 1100
F 0 "#PWR07" H 8450 950 50  0001 C CNN
F 1 "+3.3V" H 8465 1273 50  0000 C CNN
F 2 "" H 8450 1100 50  0001 C CNN
F 3 "" H 8450 1100 50  0001 C CNN
	1    8450 1100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR08
U 1 1 5F6E4743
P 8450 2200
F 0 "#PWR08" H 8450 1950 50  0001 C CNN
F 1 "GND" H 8455 2027 50  0000 C CNN
F 2 "" H 8450 2200 50  0001 C CNN
F 3 "" H 8450 2200 50  0001 C CNN
	1    8450 2200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R6
U 1 1 5F6E4E76
P 8450 1250
F 0 "R6" H 8520 1296 50  0000 L CNN
F 1 "5K" H 8520 1205 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8380 1250 50  0001 C CNN
F 3 "~" H 8450 1250 50  0001 C CNN
	1    8450 1250
	1    0    0    -1  
$EndComp
$Comp
L Device:C C3
U 1 1 5F6E5E09
P 8450 2050
F 0 "C3" H 8200 2100 50  0000 L CNN
F 1 "1uF" H 8200 2000 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 8488 1900 50  0001 C CNN
F 3 "~" H 8450 2050 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_SAMSUNG_CL21B105KBFNNNE_1uF-105-10-50V_C28323.html" H 8450 2050 50  0001 C CNN "LCSC Url"
F 5 "CL21B105KBFNNNE" H 8450 2050 50  0001 C CNN "MPN"
	1    8450 2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	8450 1900 8450 1450
Text Label 8300 1450 2    50   ~ 0
en
Wire Wire Line
	8300 1450 8450 1450
Connection ~ 8450 1450
Wire Wire Line
	8450 1450 8450 1400
$Comp
L Switch:SW_Push SW12
U 1 1 5F6E784C
P 8700 1700
F 0 "SW12" V 8654 1848 50  0000 L CNN
F 1 "reset" V 8745 1848 50  0000 L CNN
F 2 "Button_Switch_SMD:SW_Push_SPST_NO_Alps_SKRK" H 8700 1900 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1809041626_ALPS-Electric-SKRKAHE020_C202388.pdf" H 8700 1900 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Tactile-Switches_ALPS-Electric-SKRKAHE020_C202388.html" H 8700 1700 50  0001 C CNN "LCSC Url"
	1    8700 1700
	0    1    1    0   
$EndComp
Wire Wire Line
	8450 1450 8700 1450
Wire Wire Line
	8700 1450 8700 1500
Wire Wire Line
	8700 1900 8700 2200
Wire Wire Line
	8700 2200 8450 2200
Connection ~ 8450 2200
$Comp
L power:+3.3V #PWR09
U 1 1 5F6E9772
P 9150 1100
F 0 "#PWR09" H 9150 950 50  0001 C CNN
F 1 "+3.3V" H 9165 1273 50  0000 C CNN
F 2 "" H 9150 1100 50  0001 C CNN
F 3 "" H 9150 1100 50  0001 C CNN
	1    9150 1100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R7
U 1 1 5F6EA418
P 9150 1250
F 0 "R7" H 9220 1296 50  0000 L CNN
F 1 "5K" H 9220 1205 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 9080 1250 50  0001 C CNN
F 3 "~" H 9150 1250 50  0001 C CNN
	1    9150 1250
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR010
U 1 1 5F6EADDD
P 9150 2200
F 0 "#PWR010" H 9150 1950 50  0001 C CNN
F 1 "GND" H 9155 2027 50  0000 C CNN
F 2 "" H 9150 2200 50  0001 C CNN
F 3 "" H 9150 2200 50  0001 C CNN
	1    9150 2200
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW13
U 1 1 5F6EB088
P 9150 1700
F 0 "SW13" V 9104 1848 50  0000 L CNN
F 1 "bootloader" V 9195 1848 50  0000 L CNN
F 2 "Button_Switch_SMD:SW_Push_SPST_NO_Alps_SKRK" H 9150 1900 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1809041626_ALPS-Electric-SKRKAHE020_C202388.pdf" H 9150 1900 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Tactile-Switches_ALPS-Electric-SKRKAHE020_C202388.html" H 9150 1700 50  0001 C CNN "LCSC Url"
	1    9150 1700
	0    1    1    0   
$EndComp
Wire Wire Line
	9150 1400 9150 1450
Wire Wire Line
	9150 1450 9150 1500
Text Label 9050 1450 2    50   ~ 0
IO0
Connection ~ 9150 1450
Wire Wire Line
	9050 1450 9150 1450
Text Label 2550 1200 0    50   ~ 0
en
Text Label 2550 1300 0    50   ~ 0
IO0
Wire Wire Line
	2450 1300 2500 1300
Wire Wire Line
	2450 1200 2500 1200
$Comp
L Connector:TestPoint TP2
U 1 1 5F6EDDAE
P 2500 1300
F 0 "TP2" H 2450 1450 50  0000 R CNN
F 1 "TestPoint" H 2442 1417 50  0001 R CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 2700 1300 50  0001 C CNN
F 3 "~" H 2700 1300 50  0001 C CNN
	1    2500 1300
	-1   0    0    1   
$EndComp
Connection ~ 2500 1300
Wire Wire Line
	2500 1300 2550 1300
$Comp
L Connector:TestPoint TP1
U 1 1 5F6F0601
P 2500 1200
F 0 "TP1" H 2450 1400 50  0000 R CNN
F 1 "TestPoint" H 2442 1317 50  0001 R CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 2700 1200 50  0001 C CNN
F 3 "~" H 2700 1200 50  0001 C CNN
	1    2500 1200
	-1   0    0    -1  
$EndComp
Connection ~ 2500 1200
Wire Wire Line
	2500 1200 2550 1200
$Comp
L Connector_Generic:Conn_02x05_Odd_Even J4
U 1 1 5F6F1DFF
P 10100 2000
F 0 "J4" H 10150 2417 50  0000 C CNN
F 1 "JTAG" H 10150 2326 50  0000 C CNN
F 2 "Connector_IDC:IDC-Header_2x05_P2.54mm_Vertical" H 10100 2000 50  0001 C CNN
F 3 "~" H 10100 2000 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/IDC-Connectors_BOOMELE-Boom-Precision-Elec-C5665_C5665.html" H 10100 2000 50  0001 C CNN "LCSC Url"
F 5 "C5665" H 10100 2000 50  0001 C CNN "MPN"
	1    10100 2000
	1    0    0    -1  
$EndComp
Wire Notes Line
	8050 750  10800 750 
Wire Notes Line
	10800 750  10800 2800
Wire Notes Line
	10800 2800 8050 2800
Wire Notes Line
	8050 2800 8050 750 
NoConn ~ 10400 2200
Text Label 10400 2100 0    50   ~ 0
ESP_TDI
Text Label 10400 2000 0    50   ~ 0
ESP_TDO
Text Label 10400 1900 0    50   ~ 0
ESP_TCK
Text Label 10400 1800 0    50   ~ 0
ESP_TMS
Wire Wire Line
	9900 1900 9900 2000
Connection ~ 9900 2000
Wire Wire Line
	9900 2000 9900 2100
Connection ~ 9900 2100
Wire Wire Line
	9900 2100 9900 2200
Connection ~ 9900 2200
Wire Wire Line
	9900 2200 9900 2300
$Comp
L power:GND #PWR017
U 1 1 5F6F5552
P 9900 2300
F 0 "#PWR017" H 9900 2050 50  0001 C CNN
F 1 "GND" H 9905 2127 50  0000 C CNN
F 2 "" H 9900 2300 50  0001 C CNN
F 3 "" H 9900 2300 50  0001 C CNN
	1    9900 2300
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR016
U 1 1 5F6F5910
P 9900 1800
F 0 "#PWR016" H 9900 1650 50  0001 C CNN
F 1 "+3.3V" H 9915 1973 50  0000 C CNN
F 2 "" H 9900 1800 50  0001 C CNN
F 3 "" H 9900 1800 50  0001 C CNN
	1    9900 1800
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x03_Odd_Even J3
U 1 1 5F6F93CE
P 10100 1200
F 0 "J3" H 10150 1517 50  0000 C CNN
F 1 "Prog" H 10150 1426 50  0000 C CNN
F 2 "Connector_IDC:IDC-Header_2x03_P2.54mm_Vertical" H 10100 1200 50  0001 C CNN
F 3 "~" H 10100 1200 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/IDC-Connectors_BOOMELE-Boom-Precision-Elec-C11214_C11214.html" H 10100 1200 50  0001 C CNN "LCSC Url"
F 5 "C11214" H 10100 1200 50  0001 C CNN "MPN"
	1    10100 1200
	1    0    0    -1  
$EndComp
Text Label 9900 1100 2    50   ~ 0
en
Text Label 10400 1400 0    50   ~ 0
IO0
Text Label 2550 1700 0    50   ~ 0
esp_rx
Text Label 2550 1800 0    50   ~ 0
esp_tx
Wire Wire Line
	2450 1700 2500 1700
Wire Wire Line
	2450 1800 2500 1800
$Comp
L Connector:TestPoint TP3
U 1 1 5F6FC2C5
P 2500 1700
F 0 "TP3" H 2450 1850 50  0000 R CNN
F 1 "TestPoint" H 2442 1817 50  0001 R CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 2700 1700 50  0001 C CNN
F 3 "~" H 2700 1700 50  0001 C CNN
	1    2500 1700
	-1   0    0    -1  
$EndComp
Connection ~ 2500 1700
Wire Wire Line
	2500 1700 2550 1700
$Comp
L Connector:TestPoint TP4
U 1 1 5F6FCC40
P 2500 1800
F 0 "TP4" H 2450 1950 50  0000 R CNN
F 1 "TestPoint" H 2442 1917 50  0001 R CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 2700 1800 50  0001 C CNN
F 3 "~" H 2700 1800 50  0001 C CNN
	1    2500 1800
	-1   0    0    1   
$EndComp
Connection ~ 2500 1800
Wire Wire Line
	2500 1800 2550 1800
Text Label 9900 1200 2    50   ~ 0
esp_tx
Text Label 9900 1300 2    50   ~ 0
esp_rx
$Comp
L power:GND #PWR019
U 1 1 5F6FD729
P 10400 1200
F 0 "#PWR019" H 10400 950 50  0001 C CNN
F 1 "GND" V 10405 1072 50  0000 R CNN
F 2 "" H 10400 1200 50  0001 C CNN
F 3 "" H 10400 1200 50  0001 C CNN
	1    10400 1200
	0    -1   -1   0   
$EndComp
Wire Wire Line
	10400 1300 10400 1400
$Comp
L power:+3.3V #PWR018
U 1 1 5F6FE4B5
P 10400 1100
F 0 "#PWR018" H 10400 950 50  0001 C CNN
F 1 "+3.3V" H 10415 1273 50  0000 C CNN
F 2 "" H 10400 1100 50  0001 C CNN
F 3 "" H 10400 1100 50  0001 C CNN
	1    10400 1100
	1    0    0    -1  
$EndComp
Text Notes 8100 2750 0    50   ~ 0
incl. Delay Chain for \nmaking sure EN\nstays low for at least\n50 uS
$Comp
L codingfragments-mcu:ESP32-WROVER-B_(16MB) U1
U 1 1 5F704577
P 8700 2200
F 0 "U1" H 5200 3667 50  0000 C CNN
F 1 "ESP32-WROVER-B_(16MB)" H 5200 3576 50  0000 C CNN
F 2 "codingfragment-components:XCVR_ESP32-WROVER-B_(16MB)" H 2750 1900 50  0001 L BNN
F 3 "https://datasheet.octopart.com/ESP32-WROVER-B-%2816MB%29-Espressif-Systems-datasheet-137461429.pdf" H 8700 2200 50  0001 L BNN
F 4 "Manufacturer Recommendations" H 2750 1900 50  0001 L BNN "Field4"
F 5 "ESPRESSIF SYSTEMS" H 2750 1900 50  0001 L BNN "Field5"
F 6 "https://lcsc.com/product-detail/WIFI-Modules_Espressif-Systems-ESP32-WROVER-B-16MB_C529591.html" H 8700 2200 50  0001 C CNN "LCSC Url"
	1    8700 2200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR04
U 1 1 5F7094B1
P 5900 3650
F 0 "#PWR04" H 5900 3400 50  0001 C CNN
F 1 "GND" H 5905 3477 50  0000 C CNN
F 2 "" H 5900 3650 50  0001 C CNN
F 3 "" H 5900 3650 50  0001 C CNN
	1    5900 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 3650 5900 3450
Connection ~ 5900 3350
Wire Wire Line
	5900 3350 5900 3250
Connection ~ 5900 3450
Wire Wire Line
	5900 3450 5900 3350
Wire Wire Line
	5900 3250 5900 3150
Connection ~ 5900 3250
Text Label 4500 1200 2    50   ~ 0
en
Text Label 3550 2400 2    50   ~ 0
IO0
$Comp
L power:GND #PWR02
U 1 1 5F70AB2F
P 3700 2900
F 0 "#PWR02" H 3700 2650 50  0001 C CNN
F 1 "GND" H 3705 2727 50  0000 C CNN
F 2 "" H 3700 2900 50  0001 C CNN
F 3 "" H 3700 2900 50  0001 C CNN
	1    3700 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	9150 1900 9150 2200
$Comp
L Device:R R5
U 1 1 5F70E55D
P 3700 2750
F 0 "R5" H 3770 2796 50  0000 L CNN
F 1 "5K" H 3770 2705 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3630 2750 50  0001 C CNN
F 3 "~" H 3700 2750 50  0001 C CNN
	1    3700 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 2600 3700 2600
Text Label 3550 2600 2    50   ~ 0
io_neopixel
Text Notes 3400 3350 0    50   ~ 0
pulldown for\nRom Bootloader\nif IO0 is pulled
$Comp
L power:+3.3V #PWR03
U 1 1 5F70FE15
P 5900 1000
F 0 "#PWR03" H 5900 850 50  0001 C CNN
F 1 "+3.3V" H 5915 1173 50  0000 C CNN
F 2 "" H 5900 1000 50  0001 C CNN
F 3 "" H 5900 1000 50  0001 C CNN
	1    5900 1000
	1    0    0    -1  
$EndComp
$Comp
L Device:C C1
U 1 1 5F710815
P 6050 1150
F 0 "C1" H 6165 1196 50  0000 L CNN
F 1 "22uF" H 6165 1105 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 6088 1000 50  0001 C CNN
F 3 "~" H 6050 1150 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_SAMSUNG_CL31A226MOCLNNC_22uF-226-20-16V_C159758.html" H 6050 1150 50  0001 C CNN "LCSC Url"
F 5 "CL31A226MOCLNNC" H 6050 1150 50  0001 C CNN "MPN"
	1    6050 1150
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5F710FB8
P 6550 1150
F 0 "C2" H 6665 1196 50  0000 L CNN
F 1 "100nF" H 6665 1105 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 6588 1000 50  0001 C CNN
F 3 "~" H 6550 1150 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_SAMSUNG_CL21F104ZBCNNNC_100nF-104-80-20-50V_C1760.html" H 6550 1150 50  0001 C CNN "LCSC Url"
F 5 "CL21F104ZBCNNNC" H 6550 1150 50  0001 C CNN "MPN"
	1    6550 1150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR06
U 1 1 5F711311
P 6800 1300
F 0 "#PWR06" H 6800 1050 50  0001 C CNN
F 1 "GND" V 6805 1172 50  0000 R CNN
F 2 "" H 6800 1300 50  0001 C CNN
F 3 "" H 6800 1300 50  0001 C CNN
	1    6800 1300
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6050 1300 6550 1300
Connection ~ 6550 1300
Wire Wire Line
	6550 1300 6800 1300
Wire Wire Line
	6550 1000 6050 1000
Connection ~ 5900 1000
Connection ~ 6050 1000
Wire Wire Line
	6050 1000 5900 1000
Text Label 4500 1500 2    50   ~ 0
esp_tx
Text Label 4500 1400 2    50   ~ 0
esp_rx
Text Label 5900 2900 0    50   ~ 0
ESP_TDO
Text Label 4500 2900 2    50   ~ 0
ESP_TDI
Text Label 4500 3000 2    50   ~ 0
ESP_TCK
Text Label 5900 3000 0    50   ~ 0
ESP_TMS
Text Label 5900 1500 0    50   ~ 0
io_in0
Text Label 5900 1400 0    50   ~ 0
io_in1
Text Label 5900 1800 0    50   ~ 0
io_in2
Text Label 5900 1700 0    50   ~ 0
io_in3
Text Label 5900 2000 0    50   ~ 0
io_sel0
Text Label 5900 1900 0    50   ~ 0
io_sel1
Text Label 5900 2300 0    50   ~ 0
io_sel2
Text Label 5900 2200 0    50   ~ 0
io_speaker
Text Label 5900 2100 0    50   ~ 0
io_rot_b
NoConn ~ 4500 2100
NoConn ~ 4500 2200
NoConn ~ 4500 2300
NoConn ~ 4500 1700
NoConn ~ 4500 1800
NoConn ~ 4500 1900
Wire Notes Line
	4300 1650 4400 1650
Wire Notes Line
	4400 1650 4400 2350
Wire Notes Line
	4400 2350 4300 2350
Wire Notes Line
	4300 2350 4300 1650
Text Notes 4400 1900 3    50   ~ 0
FLASH
Text Label 5900 2400 0    50   ~ 0
disp_din
Text Label 5900 2800 0    50   ~ 0
disp_clk
Text Label 4500 2800 2    50   ~ 0
disp_cs
Text Label 4500 2700 2    50   ~ 0
disp_busy
Text Label 5900 2700 0    50   ~ 0
io_rot_a
Text Label 5900 2500 0    50   ~ 0
disp_dc
Text Label 5900 2600 0    50   ~ 0
disp_rst
$Comp
L Connector:Conn_01x08_Male J1
U 1 1 5F66C748
P 9400 3650
F 0 "J1" H 9650 4200 50  0000 C CNN
F 1 "Display" H 9750 4100 50  0000 C CNN
F 2 "Connector_JST:JST_PH_S8B-PH-SM4-TB_1x08-1MP_P2.00mm_Horizontal" H 9400 3650 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1912111437_JST-Sales-America-S8B-PH-SM4-TB-LF-SN_C265121.pdf" H 9400 3650 50  0001 C CNN
F 4 "" H 9400 3650 50  0001 C CNN "lcsc"
F 5 "https://lcsc.com/product-detail/New-Arrivals_JST-Sales-America-S8B-PH-SM4-TB-LF-SN_C265121.html" H 9400 3650 50  0001 C CNN "LCSC Url"
F 6 "https://lcsc.com/product-detail/Rectangular-Connectors-Contacts_JST_SPH-002T-P0-5S_SPH-002T-P0-5S-PH-T-PH-2-0_C111515.html , https://lcsc.com/product-detail/Rectangular-Connectors-Housings_JST-Sales-America_PHR-8_JST-Sales-America-PHR-8_C157950.html" H 9400 3650 50  0001 C CNN "Alternative"
	1    9400 3650
	1    0    0    -1  
$EndComp
Text Label 9600 3350 0    50   ~ 0
disp_busy
Text Label 9600 3450 0    50   ~ 0
disp_rst
Text Label 9600 3550 0    50   ~ 0
disp_dc
Text Label 9600 3650 0    50   ~ 0
disp_cs
Text Label 9600 3750 0    50   ~ 0
disp_clk
Text Label 9600 3850 0    50   ~ 0
disp_din
$Comp
L power:+3.3V #PWR011
U 1 1 5F671F4B
P 9600 4150
F 0 "#PWR011" H 9600 4000 50  0001 C CNN
F 1 "+3.3V" H 9615 4323 50  0000 C CNN
F 2 "" H 9600 4150 50  0001 C CNN
F 3 "" H 9600 4150 50  0001 C CNN
	1    9600 4150
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR015
U 1 1 5F6727C0
P 9850 4150
F 0 "#PWR015" H 9850 3900 50  0001 C CNN
F 1 "GND" H 9855 3977 50  0000 C CNN
F 2 "" H 9850 4150 50  0001 C CNN
F 3 "" H 9850 4150 50  0001 C CNN
	1    9850 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	9600 4050 9600 4150
Wire Wire Line
	9600 3950 9850 3950
Wire Wire Line
	9850 3950 9850 4150
$Comp
L Device:Rotary_Encoder_Switch SW11
U 1 1 5F674A4F
P 6250 6150
F 0 "SW11" V 6400 6500 50  0000 C CNN
F 1 "Rotary_Encoder_Switch" V 6250 6800 50  0001 C CNN
F 2 "Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm" H 6100 6310 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1809181724_ALPS-Electric-EC11E1534408_C278348.pdf" H 6250 6410 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Coded-Rotary-Switches_ALPS-Electric-EC11E1534408_C278348.html" H 6250 6150 50  0001 C CNN "LCSC Url"
F 5 "https://lcsc.com/product-detail/Coded-Rotary-Switches_ALPS-Electric-EC11J1525402_C209762.html" V 6250 6150 50  0001 C CNN "Alternative"
	1    6250 6150
	0    1    -1   0   
$EndComp
$Comp
L power:GND #PWR05
U 1 1 5F67803A
P 6250 6850
F 0 "#PWR05" H 6250 6600 50  0001 C CNN
F 1 "GND" H 6255 6677 50  0000 C CNN
F 2 "" H 6250 6850 50  0001 C CNN
F 3 "" H 6250 6850 50  0001 C CNN
	1    6250 6850
	-1   0    0    -1  
$EndComp
Text Label 6050 6450 2    50   ~ 0
io_rot_b
Text Label 6450 6450 0    50   ~ 0
io_rot_a
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW1
U 1 1 5F67EB8A
P 3900 4550
F 0 "SW1" H 3900 4533 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 3900 4534 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 4730 5200 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 3900 4550 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 4480 5110 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 4680 5030 50  0001 C CNN "LCSC Url"
	1    3900 4550
	1    0    0    -1  
$EndComp
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW2
U 1 1 5F68028B
P 3900 5200
F 0 "SW2" H 3900 5183 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 3900 5184 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 4730 5850 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 3900 5200 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 4480 5760 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 4680 5680 50  0001 C CNN "LCSC Url"
	1    3900 5200
	1    0    0    -1  
$EndComp
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW3
U 1 1 5F680F0E
P 3900 5700
F 0 "SW3" H 3900 5683 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 3900 5684 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 4730 6350 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 3900 5700 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 4480 6260 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 4680 6180 50  0001 C CNN "LCSC Url"
	1    3900 5700
	1    0    0    -1  
$EndComp
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW4
U 1 1 5F6816D2
P 3900 6300
F 0 "SW4" H 3900 6283 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 3900 6284 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 4730 6950 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 3900 6300 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 4480 6860 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 4680 6780 50  0001 C CNN "LCSC Url"
	1    3900 6300
	1    0    0    -1  
$EndComp
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW5
U 1 1 5F682193
P 5050 4550
F 0 "SW5" H 5050 4533 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 5050 4534 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 5880 5200 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 5050 4550 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 5630 5110 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 5830 5030 50  0001 C CNN "LCSC Url"
	1    5050 4550
	1    0    0    -1  
$EndComp
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW6
U 1 1 5F683389
P 5050 5200
F 0 "SW6" H 5050 5183 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 5050 5184 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 5880 5850 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 5050 5200 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 5630 5760 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 5830 5680 50  0001 C CNN "LCSC Url"
	1    5050 5200
	1    0    0    -1  
$EndComp
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW7
U 1 1 5F683ED1
P 5050 5700
F 0 "SW7" H 5050 5683 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 5050 5684 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 5880 6350 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 5050 5700 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 5630 6260 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 5830 6180 50  0001 C CNN "LCSC Url"
	1    5050 5700
	1    0    0    -1  
$EndComp
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW8
U 1 1 5F68525F
P 5050 6300
F 0 "SW8" H 5050 6283 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 5050 6284 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 5880 6950 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 5050 6300 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 5630 6860 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 5830 6780 50  0001 C CNN "LCSC Url"
	1    5050 6300
	1    0    0    -1  
$EndComp
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW9
U 1 1 5F685F0F
P 6250 4550
F 0 "SW9" H 6250 4533 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 6250 4534 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 7080 5200 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 6250 4550 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 6830 5110 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 7030 5030 50  0001 C CNN "LCSC Url"
	1    6250 4550
	1    0    0    -1  
$EndComp
$Comp
L Codingfragments_switches:TactileSwitchSMD6x6 SW10
U 1 1 5F687132
P 6250 5200
F 0 "SW10" H 6250 5183 50  0000 C CNN
F 1 "TactileSwitchSMD6x6" H 6250 5184 50  0001 C CNN
F 2 "digikey-footprints:Switch_Tactile_SMD_6x6mm" H 7080 5850 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/1811011023_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.pdf" H 6250 5200 50  0001 C CNN
F 4 "1TS005F-2500-5001" H 6830 5760 50  0001 C CNN "MPN"
F 5 "https://lcsc.com/product-detail/Tactile-Switches_HYP-Hongyuan-Precision-1TS005F-2500-5001_C255812.html" H 7030 5680 50  0001 C CNN "LCSC Url"
	1    6250 5200
	1    0    0    -1  
$EndComp
Text Label 3350 5000 2    50   ~ 0
io_in0
Text Label 3350 5650 2    50   ~ 0
io_in1
Text Label 3350 6200 2    50   ~ 0
io_in2
Text Label 3350 6750 2    50   ~ 0
io_in3
Text Label 4100 4400 1    50   ~ 0
io_sel0
Text Label 5250 4400 1    50   ~ 0
io_sel1
Text Label 6450 4400 1    50   ~ 0
io_sel2
Wire Wire Line
	6450 4400 6450 4450
Wire Wire Line
	6450 4700 6450 4900
Connection ~ 6450 4700
Connection ~ 6450 4900
Wire Wire Line
	6450 4900 6450 5350
Connection ~ 6450 5350
Wire Wire Line
	6450 5350 6450 5550
Wire Wire Line
	6450 5550 6450 5850
Wire Wire Line
	6450 5850 6350 5850
Connection ~ 6450 5550
Wire Wire Line
	5250 4400 5250 4450
Connection ~ 5250 4700
Wire Wire Line
	5250 4700 5250 4900
Connection ~ 5250 4900
Wire Wire Line
	5250 4900 5250 5350
Connection ~ 5250 5350
Wire Wire Line
	5250 5350 5250 5550
Connection ~ 5250 5550
Wire Wire Line
	5250 5550 5250 5850
Connection ~ 5250 5850
Wire Wire Line
	5250 5850 5250 6050
Connection ~ 5250 6050
Wire Wire Line
	5250 6050 5250 6450
Connection ~ 5250 6450
Wire Wire Line
	5250 6450 5250 6650
Wire Wire Line
	4100 4400 4100 4450
Connection ~ 4100 4700
Wire Wire Line
	4100 4700 4100 4900
Connection ~ 4100 4900
Wire Wire Line
	4100 4900 4100 5350
Connection ~ 4100 5350
Wire Wire Line
	4100 5350 4100 5550
Connection ~ 4100 5550
Wire Wire Line
	4100 5550 4100 5850
Connection ~ 4100 5850
Wire Wire Line
	4100 5850 4100 6050
Connection ~ 4100 6050
Wire Wire Line
	4100 6050 4100 6450
Connection ~ 4100 6450
Wire Wire Line
	4100 6450 4100 6650
$Comp
L Device:D_Small_ALT D1
U 1 1 5F6B4294
P 3550 5000
F 0 "D1" V 3550 4930 50  0000 R CNN
F 1 "D_Small_ALT" H 3550 5116 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 3550 5000 50  0001 C CNN
F 3 "~" V 3550 5000 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 3550 5000 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 3550 5000 50  0001 C CNN "MPN"
	1    3550 5000
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D2
U 1 1 5F6B6AA8
P 3550 5650
F 0 "D2" V 3550 5580 50  0000 R CNN
F 1 "D_Small_ALT" H 3550 5766 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 3550 5650 50  0001 C CNN
F 3 "~" V 3550 5650 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 3550 5650 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 3550 5650 50  0001 C CNN "MPN"
	1    3550 5650
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D3
U 1 1 5F6B7058
P 3550 6150
F 0 "D3" V 3550 6080 50  0000 R CNN
F 1 "D_Small_ALT" H 3550 6266 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 3550 6150 50  0001 C CNN
F 3 "~" V 3550 6150 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 3550 6150 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 3550 6150 50  0001 C CNN "MPN"
	1    3550 6150
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D4
U 1 1 5F6B7491
P 3550 6750
F 0 "D4" V 3550 6680 50  0000 R CNN
F 1 "D_Small_ALT" H 3550 6866 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 3550 6750 50  0001 C CNN
F 3 "~" V 3550 6750 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 3550 6750 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 3550 6750 50  0001 C CNN "MPN"
	1    3550 6750
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D5
U 1 1 5F6BC945
P 4700 5000
F 0 "D5" V 4700 4930 50  0000 R CNN
F 1 "D_Small_ALT" H 4700 5116 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 4700 5000 50  0001 C CNN
F 3 "~" V 4700 5000 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 4700 5000 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 4700 5000 50  0001 C CNN "MPN"
	1    4700 5000
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D9
U 1 1 5F6BD134
P 5900 5000
F 0 "D9" V 5900 4930 50  0000 R CNN
F 1 "D_Small_ALT" H 5900 5116 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 5900 5000 50  0001 C CNN
F 3 "~" V 5900 5000 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 5900 5000 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 5900 5000 50  0001 C CNN "MPN"
	1    5900 5000
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D10
U 1 1 5F6BD8D8
P 5900 5650
F 0 "D10" V 5900 5580 50  0000 R CNN
F 1 "D_Small_ALT" H 5900 5766 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 5900 5650 50  0001 C CNN
F 3 "~" V 5900 5650 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 5900 5650 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 5900 5650 50  0001 C CNN "MPN"
	1    5900 5650
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D6
U 1 1 5F6BDE3D
P 4700 5650
F 0 "D6" V 4700 5580 50  0000 R CNN
F 1 "D_Small_ALT" H 4700 5766 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 4700 5650 50  0001 C CNN
F 3 "~" V 4700 5650 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 4700 5650 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 4700 5650 50  0001 C CNN "MPN"
	1    4700 5650
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D7
U 1 1 5F6BE3ED
P 4700 6150
F 0 "D7" V 4700 6080 50  0000 R CNN
F 1 "D_Small_ALT" H 4700 6266 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 4700 6150 50  0001 C CNN
F 3 "~" V 4700 6150 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 4700 6150 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 4700 6150 50  0001 C CNN "MPN"
	1    4700 6150
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D8
U 1 1 5F6BEB46
P 4700 6750
F 0 "D8" V 4700 6680 50  0000 R CNN
F 1 "D_Small_ALT" H 4700 6866 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 4700 6750 50  0001 C CNN
F 3 "~" V 4700 6750 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 4700 6750 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 4700 6750 50  0001 C CNN "MPN"
	1    4700 6750
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D11
U 1 1 5F6BF02E
P 5900 6150
F 0 "D11" V 5900 6080 50  0000 R CNN
F 1 "D_Small_ALT" H 5900 6266 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 5900 6150 50  0001 C CNN
F 3 "~" V 5900 6150 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 5900 6150 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 5900 6150 50  0001 C CNN "MPN"
	1    5900 6150
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5900 6250 4700 6250
Connection ~ 3550 6250
Wire Wire Line
	3550 6250 3350 6250
Connection ~ 4700 6250
Wire Wire Line
	4700 6250 3550 6250
Wire Wire Line
	5900 5750 4700 5750
Connection ~ 4700 5750
Wire Wire Line
	4700 5750 3550 5750
Wire Wire Line
	5900 5100 4700 5100
Connection ~ 3550 5100
Wire Wire Line
	3550 5100 3350 5100
Connection ~ 4700 5100
Wire Wire Line
	4700 5100 3550 5100
Wire Wire Line
	3700 4900 3550 4900
Wire Wire Line
	4850 4900 4700 4900
Wire Wire Line
	6050 4900 5900 4900
Wire Wire Line
	6050 5550 5900 5550
Wire Wire Line
	6050 5350 6050 5550
Connection ~ 6050 5550
Wire Wire Line
	4850 5350 4850 5550
Wire Wire Line
	4700 5550 4850 5550
Connection ~ 4850 5550
Wire Wire Line
	3700 5350 3700 5550
Wire Wire Line
	3550 5550 3700 5550
Connection ~ 3700 5550
Connection ~ 3550 5750
Wire Wire Line
	3550 5750 3350 5750
Wire Wire Line
	3700 4700 3700 4900
Connection ~ 3700 4900
Wire Wire Line
	4850 4700 4850 4900
Connection ~ 4850 4900
Wire Wire Line
	6050 4700 6050 4900
Connection ~ 6050 4900
Wire Wire Line
	6150 5850 5900 5850
Wire Wire Line
	5900 5850 5900 6050
Wire Wire Line
	4850 5850 4850 6050
Wire Wire Line
	4700 6050 4850 6050
Connection ~ 4850 6050
Wire Wire Line
	3700 5850 3700 6050
Wire Wire Line
	3700 6050 3550 6050
Connection ~ 3700 6050
Wire Wire Line
	3700 6450 3700 6650
Wire Wire Line
	3550 6650 3700 6650
Connection ~ 3700 6650
Wire Wire Line
	4850 6450 4850 6650
Wire Wire Line
	4850 6650 4700 6650
Connection ~ 4850 6650
Wire Wire Line
	4700 6850 3550 6850
Connection ~ 3550 6850
Wire Wire Line
	3550 6850 3350 6850
$Comp
L Connector:Conn_01x02_Male J2
U 1 1 5F701323
P 9400 5050
F 0 "J2" H 9600 5300 50  0000 C CNN
F 1 "speaker" H 9600 5200 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Horizontal" H 9400 5050 50  0001 C CNN
F 3 "~" H 9400 5050 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Pin-Header-Female-Header_MINTRON-MTB125-1102R1_C376120.html" H 9400 5050 50  0001 C CNN "LCSC Url"
	1    9400 5050
	1    0    0    -1  
$EndComp
Text Label 9600 5050 0    50   ~ 0
io_speaker
$Comp
L power:GND #PWR012
U 1 1 5F702FA2
P 9600 5150
F 0 "#PWR012" H 9600 4900 50  0001 C CNN
F 1 "GND" H 9605 4977 50  0000 C CNN
F 2 "" H 9600 5150 50  0001 C CNN
F 3 "" H 9600 5150 50  0001 C CNN
	1    9600 5150
	1    0    0    -1  
$EndComp
$Comp
L Device:C C4
U 1 1 5F704A2D
P 9850 5750
F 0 "C4" H 9965 5796 50  0000 L CNN
F 1 "22uF" H 9965 5705 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 9888 5600 50  0001 C CNN
F 3 "~" H 9850 5750 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_SAMSUNG_CL31A226MOCLNNC_22uF-226-20-16V_C159758.html" H 9850 5750 50  0001 C CNN "LCSC Url"
F 5 "CL31A226MOCLNNC" H 9850 5750 50  0001 C CNN "MPN"
	1    9850 5750
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR014
U 1 1 5F70BE0B
P 9650 5600
F 0 "#PWR014" H 9650 5450 50  0001 C CNN
F 1 "+3.3V" H 9665 5773 50  0000 C CNN
F 2 "" H 9650 5600 50  0001 C CNN
F 3 "" H 9650 5600 50  0001 C CNN
	1    9650 5600
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR013
U 1 1 5F70C859
P 9600 5900
F 0 "#PWR013" H 9600 5650 50  0001 C CNN
F 1 "GND" H 9605 5727 50  0000 C CNN
F 2 "" H 9600 5900 50  0001 C CNN
F 3 "" H 9600 5900 50  0001 C CNN
	1    9600 5900
	1    0    0    -1  
$EndComp
Wire Wire Line
	9650 5600 9850 5600
Wire Wire Line
	9600 5900 9850 5900
$Sheet
S 900  3300 1550 1200
U 5F74EBF4
F0 "ws2812B" 50
F1 "LEDs.sch" 50
F2 "ws2812B-DIN" I R 2450 3700 50 
$EndSheet
Text Label 2600 3700 0    50   ~ 0
io_neopixel
Wire Wire Line
	2600 3700 2450 3700
Text Notes 1800 4450 0    50   ~ 0
12 * ws2812B\n
$Comp
L Device:R R1
U 1 1 5F66C2BC
P 3200 5300
F 0 "R1" V 2993 5300 50  0000 C CNN
F 1 "10K" V 3084 5300 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3130 5300 50  0001 C CNN
F 3 "~" H 3200 5300 50  0001 C CNN
	1    3200 5300
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 5F66FFB4
P 3200 5950
F 0 "R2" V 2993 5950 50  0000 C CNN
F 1 "10K" V 3084 5950 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3130 5950 50  0001 C CNN
F 3 "~" H 3200 5950 50  0001 C CNN
	1    3200 5950
	0    1    1    0   
$EndComp
$Comp
L Device:R R3
U 1 1 5F67050F
P 3200 6500
F 0 "R3" V 2993 6500 50  0000 C CNN
F 1 "10K" V 3084 6500 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3130 6500 50  0001 C CNN
F 3 "~" H 3200 6500 50  0001 C CNN
	1    3200 6500
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 5F67092F
P 3200 7000
F 0 "R4" V 2993 7000 50  0000 C CNN
F 1 "10K" V 3084 7000 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3130 7000 50  0001 C CNN
F 3 "~" H 3200 7000 50  0001 C CNN
	1    3200 7000
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR01
U 1 1 5F670F86
P 3050 7400
F 0 "#PWR01" H 3050 7150 50  0001 C CNN
F 1 "GND" H 3055 7227 50  0000 C CNN
F 2 "" H 3050 7400 50  0001 C CNN
F 3 "" H 3050 7400 50  0001 C CNN
	1    3050 7400
	1    0    0    -1  
$EndComp
Wire Wire Line
	3050 5300 3050 5950
Connection ~ 3050 5950
Wire Wire Line
	3050 5950 3050 6500
Connection ~ 3050 6500
Wire Wire Line
	3050 6500 3050 7000
Connection ~ 3050 7000
Wire Wire Line
	3050 7000 3050 7400
Wire Wire Line
	3350 7000 3350 6850
Wire Wire Line
	3350 6500 3350 6250
Wire Wire Line
	3350 5950 3350 5750
Wire Wire Line
	3350 5300 3350 5100
Wire Wire Line
	3350 6750 3350 6850
Connection ~ 3350 6850
Wire Wire Line
	3350 6200 3350 6250
Connection ~ 3350 6250
Wire Wire Line
	3350 5650 3350 5750
Connection ~ 3350 5750
Wire Wire Line
	3350 5000 3350 5100
Connection ~ 3350 5100
$Comp
L ProjectParts:EInkDisplay-2.9 Disp1
U 1 1 5F742A38
P 8700 3300
F 0 "Disp1" H 8650 3350 50  0000 L CNN
F 1 "EInkDisplay-2.9" H 8450 2800 50  0000 L CNN
F 2 "ProjectParts:EInkDisplay2.9" H 8700 3300 50  0001 C CNN
F 3 "" H 8700 3300 50  0001 C CNN
	1    8700 3300
	1    0    0    -1  
$EndComp
Connection ~ 3700 2600
Wire Wire Line
	3700 2600 4500 2600
Wire Wire Line
	3550 2500 3700 2500
Wire Wire Line
	3550 2400 3700 2400
Wire Wire Line
	3700 2400 3700 2500
Connection ~ 3700 2500
Wire Wire Line
	3700 2500 3850 2500
$Comp
L Connector:Conn_01x02_Male SW14
U 1 1 5F94C13A
P 6150 7350
F 0 "SW14" V 6250 7200 50  0000 R CNN
F 1 "Conn_01x02_Male" V 6100 7600 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 6150 7350 50  0001 C CNN
F 3 "~" H 6150 7350 50  0001 C CNN
	1    6150 7350
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small_ALT D30
U 1 1 5F94D9D7
P 5700 7050
F 0 "D30" V 5700 6980 50  0000 R CNN
F 1 "D_Small_ALT" H 5700 7166 50  0001 C CNN
F 2 "Diode_SMD:D_SOT-23_ANK" V 5700 7050 50  0001 C CNN
F 3 "~" V 5700 7050 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Switching-Diode_DIODES_BAV99-7-F_BAV99-7-F_C106919.html" H 5700 7050 50  0001 C CNN "LCSC Url"
F 5 "BAV99-7-F" H 5700 7050 50  0001 C CNN "MPN"
	1    5700 7050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 7050 5600 6850
Wire Wire Line
	5600 6850 4700 6850
Connection ~ 4700 6850
Wire Wire Line
	6150 7150 5800 7150
Wire Wire Line
	5800 7150 5800 7050
Wire Wire Line
	6450 5850 6800 5850
Wire Wire Line
	6800 5850 6800 7150
Wire Wire Line
	6800 7150 6250 7150
Connection ~ 6450 5850
$Comp
L Connector:TestPoint TP9
U 1 1 5F9425B0
P 3850 2500
F 0 "TP9" H 3908 2618 50  0000 L CNN
F 1 "TestPoint" H 3908 2527 50  0000 L CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 4050 2500 50  0001 C CNN
F 3 "~" H 4050 2500 50  0001 C CNN
	1    3850 2500
	1    0    0    -1  
$EndComp
Connection ~ 3850 2500
Wire Wire Line
	3850 2500 4500 2500
$Comp
L Connector:TestPoint TP10
U 1 1 5F942E55
P 4100 4450
F 0 "TP10" V 4054 4638 50  0000 L CNN
F 1 "TestPoint" V 4145 4638 50  0000 L CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 4300 4450 50  0001 C CNN
F 3 "~" H 4300 4450 50  0001 C CNN
	1    4100 4450
	0    1    1    0   
$EndComp
Connection ~ 4100 4450
Wire Wire Line
	4100 4450 4100 4700
$Comp
L Connector:TestPoint TP11
U 1 1 5F943752
P 5250 4450
F 0 "TP11" V 5204 4638 50  0000 L CNN
F 1 "TestPoint" V 5295 4638 50  0000 L CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 5450 4450 50  0001 C CNN
F 3 "~" H 5450 4450 50  0001 C CNN
	1    5250 4450
	0    1    1    0   
$EndComp
Connection ~ 5250 4450
Wire Wire Line
	5250 4450 5250 4700
$Comp
L Connector:TestPoint TP12
U 1 1 5F943B6F
P 6450 4450
F 0 "TP12" V 6404 4638 50  0000 L CNN
F 1 "TestPoint" V 6495 4638 50  0000 L CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 6650 4450 50  0001 C CNN
F 3 "~" H 6650 4450 50  0001 C CNN
	1    6450 4450
	0    1    1    0   
$EndComp
Connection ~ 6450 4450
Wire Wire Line
	6450 4450 6450 4700
$Comp
L Device:R R14
U 1 1 5FA8EF1B
P 6050 6600
F 0 "R14" H 5850 6650 50  0000 L CNN
F 1 "10K" H 5850 6550 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5980 6600 50  0001 C CNN
F 3 "~" H 6050 6600 50  0001 C CNN
	1    6050 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 6450 6050 6450
$Comp
L Device:R R15
U 1 1 5FA94F2B
P 6450 6600
F 0 "R15" H 6520 6646 50  0000 L CNN
F 1 "10K" H 6520 6555 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6380 6600 50  0001 C CNN
F 3 "~" H 6450 6600 50  0001 C CNN
	1    6450 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	6350 6450 6450 6450
$Comp
L power:+3.3V #PWR036
U 1 1 5FA9A3EE
P 6050 6750
F 0 "#PWR036" H 6050 6600 50  0001 C CNN
F 1 "+3.3V" H 6065 6923 50  0000 C CNN
F 2 "" H 6050 6750 50  0001 C CNN
F 3 "" H 6050 6750 50  0001 C CNN
	1    6050 6750
	-1   0    0    1   
$EndComp
Wire Wire Line
	6250 6450 6250 6850
Wire Wire Line
	6450 6750 6050 6750
Connection ~ 6050 6750
$EndSCHEMATC
