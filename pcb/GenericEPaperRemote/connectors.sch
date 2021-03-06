EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Interface_USB:FT232RL U2
U 1 1 5F59A8FB
P 3700 2850
F 0 "U2" H 3950 3900 50  0000 C CNN
F 1 "FT232RL" H 4050 3750 50  0000 C CNN
F 2 "Package_SO:SSOP-28_5.3x10.2mm_P0.65mm" H 4800 1950 50  0001 C CNN
F 3 "https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232R.pdf" H 3700 2850 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/USB-ICs_FTDI_FT232RL-REEL_FTDI-FT232RL-REEL_C8690.html" H 3700 2850 50  0001 C CNN "LCSC Url"
	1    3700 2850
	1    0    0    -1  
$EndComp
$Comp
L Connector:USB_B_Micro USB1
U 1 1 5F5E32B0
P 1000 1800
F 0 "USB1" H 1057 2267 50  0000 C CNN
F 1 "USB-Vertical" H 1057 2176 50  0000 C CNN
F 2 "Connector_USB:USB_Micro-B_Molex-105133-0031" H 1150 1750 50  0001 C CNN
F 3 "~" H 1150 1750 50  0001 C CNN
F 4 "https://www.digikey.de/product-detail/en/1051330031/900-1051330031CT-ND/12417585?utm_campaign=buynow&utm_medium=aggregator&curr=eur&utm_source=octopart" H 1000 1800 50  0001 C CNN "Alternative"
F 5 "https://lcsc.com/product-detail/Pre-ordered-Products_MOLEX_1051330011_MOLEX-1051330011_C586226.html" H 1000 1800 50  0001 C CNN "LCSC Url"
	1    1000 1800
	1    0    0    -1  
$EndComp
NoConn ~ 1300 2000
Wire Wire Line
	1300 1600 1650 1600
Text Label 1300 1800 0    50   ~ 0
usb_d+
Text Label 1300 1900 0    50   ~ 0
usb_d-
$Comp
L power:GND #PWR023
U 1 1 5F5E7413
P 1650 2300
F 0 "#PWR023" H 1650 2050 50  0001 C CNN
F 1 "GND" H 1655 2127 50  0000 C CNN
F 2 "" H 1650 2300 50  0001 C CNN
F 3 "" H 1650 2300 50  0001 C CNN
	1    1650 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	900  2200 1000 2200
Wire Wire Line
	1000 2200 1650 2200
Wire Wire Line
	1650 2200 1650 2300
Connection ~ 1000 2200
$Comp
L Device:C C5
U 1 1 5F5E7C9F
P 1650 2050
F 0 "C5" H 1765 2096 50  0000 L CNN
F 1 "10nF" H 1765 2005 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 1688 1900 50  0001 C CNN
F 3 "~" H 1650 2050 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_SAMSUNG_CL21B103KBCNNNC_10nF-103-10-50V_C84715.html" H 1650 2050 50  0001 C CNN "LCSC Url"
F 5 "CL21B103KBCNNNC" H 1650 2050 50  0001 C CNN "MPN"
	1    1650 2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	1650 1900 1650 1600
Text Label 1300 1600 0    50   ~ 0
usb_v+
$Comp
L Device:C_Small C6
U 1 1 5F5F0448
P 2500 2250
F 0 "C6" H 2592 2296 50  0000 L CNN
F 1 "100nF" H 2592 2205 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 2500 2250 50  0001 C CNN
F 3 "~" H 2500 2250 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_SAMSUNG_CL21F104ZBCNNNC_100nF-104-80-20-50V_C1760.html" H 2500 2250 50  0001 C CNN "LCSC Url"
F 5 "CL21F104ZBCNNNC" H 2500 2250 50  0001 C CNN "MPN"
	1    2500 2250
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR024
U 1 1 5F5F12ED
P 2500 2350
F 0 "#PWR024" H 2500 2100 50  0001 C CNN
F 1 "GND" H 2505 2177 50  0000 C CNN
F 2 "" H 2500 2350 50  0001 C CNN
F 3 "" H 2500 2350 50  0001 C CNN
	1    2500 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 2150 2850 2150
Text Label 2900 2450 2    50   ~ 0
usb_d+
Text Label 2900 2550 2    50   ~ 0
usb_d-
NoConn ~ 2900 2850
NoConn ~ 2900 3050
NoConn ~ 2900 3250
NoConn ~ 2900 3550
$Comp
L power:GND #PWR025
U 1 1 5F5F2369
P 3700 4000
F 0 "#PWR025" H 3700 3750 50  0001 C CNN
F 1 "GND" H 3705 3827 50  0000 C CNN
F 2 "" H 3700 4000 50  0001 C CNN
F 3 "" H 3700 4000 50  0001 C CNN
	1    3700 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 3850 3700 3850
Wire Wire Line
	3700 3850 3700 4000
Connection ~ 3700 3850
Wire Wire Line
	3800 3850 3700 3850
Wire Wire Line
	3900 3850 3800 3850
Connection ~ 3800 3850
NoConn ~ 4500 3350
NoConn ~ 4500 3450
NoConn ~ 4500 3550
Connection ~ 1650 2200
$Comp
L Connector:Conn_01x06_Male USB2
U 1 1 5F5FB70F
P 1150 3350
F 0 "USB2" H 1150 3700 50  0000 C CNN
F 1 "USB_PCBConnector" H 1800 3700 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 1150 3350 50  0001 C CNN
F 3 "~" H 1150 3350 50  0001 C CNN
	1    1150 3350
	1    0    0    -1  
$EndComp
Text Label 1350 3150 0    50   ~ 0
usb_v+
Text Label 1350 3350 0    50   ~ 0
usb_d+
Text Label 1350 3250 0    50   ~ 0
usb_d-
$Comp
L power:GND #PWR021
U 1 1 5F5FF211
P 1550 3550
F 0 "#PWR021" H 1550 3300 50  0001 C CNN
F 1 "GND" H 1555 3377 50  0000 C CNN
F 2 "" H 1550 3550 50  0001 C CNN
F 3 "" H 1550 3550 50  0001 C CNN
	1    1550 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	3600 1850 2850 1850
Wire Wire Line
	2850 1850 2850 2150
Connection ~ 2850 2150
Wire Wire Line
	2850 2150 2900 2150
Wire Wire Line
	2250 1600 2400 1600
Wire Wire Line
	3800 1600 3800 1850
Wire Wire Line
	1950 1600 1650 1600
Connection ~ 1650 1600
$Comp
L Device:LED D14
U 1 1 5F6039B1
P 4900 3600
F 0 "D14" V 4847 3678 50  0000 L CNN
F 1 "Green" V 4938 3678 50  0000 L CNN
F 2 "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 4900 3600 50  0001 C CNN
F 3 "~" H 4900 3600 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Others_TOGIALED-TJ-1206G-01_C192678.html" H 4900 3600 50  0001 C CNN "LCSC Url"
F 5 "TJ-S3216SW9TGLC2G-A5" H 4900 3600 50  0001 C CNN "MPN"
	1    4900 3600
	0    1    1    0   
$EndComp
$Comp
L Device:LED D15
U 1 1 5F605FA5
P 5400 3600
F 0 "D15" V 5350 3800 50  0000 R CNN
F 1 "Red" V 5450 3800 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 5400 3600 50  0001 C CNN
F 3 "~" H 5400 3600 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Others_TOGIALED-TJ-S1206R-01_C192674.html" H 5400 3600 50  0001 C CNN "LCSC Url"
F 5 "TJ-S3216SW9TGLC2R-A5" H 5400 3600 50  0001 C CNN "MPN"
	1    5400 3600
	0    1    1    0   
$EndComp
Wire Wire Line
	4900 3250 4500 3250
Wire Wire Line
	5400 3150 4500 3150
$Comp
L Device:R R8
U 1 1 5F60A706
P 4900 3900
F 0 "R8" H 4970 3946 50  0000 L CNN
F 1 "270R" H 4970 3855 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 4830 3900 50  0001 C CNN
F 3 "~" H 4900 3900 50  0001 C CNN
	1    4900 3900
	1    0    0    -1  
$EndComp
$Comp
L Device:R R9
U 1 1 5F60A75C
P 5400 3900
F 0 "R9" H 5470 3946 50  0000 L CNN
F 1 "270R" H 5470 3855 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5330 3900 50  0001 C CNN
F 3 "~" H 5400 3900 50  0001 C CNN
	1    5400 3900
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR026
U 1 1 5F60BDC7
P 5150 4150
F 0 "#PWR026" H 5150 4000 50  0001 C CNN
F 1 "+3.3V" H 5165 4323 50  0000 C CNN
F 2 "" H 5150 4150 50  0001 C CNN
F 3 "" H 5150 4150 50  0001 C CNN
	1    5150 4150
	-1   0    0    1   
$EndComp
Wire Wire Line
	4900 3450 4900 3250
Wire Wire Line
	5400 3150 5400 3450
Wire Wire Line
	5150 4150 4900 4150
Wire Wire Line
	4900 4150 4900 4050
Wire Wire Line
	5150 4150 5400 4150
Wire Wire Line
	5400 4150 5400 4050
Connection ~ 5150 4150
Text Label 3800 1600 0    50   ~ 0
usb_v_ext
$Comp
L Regulator_Linear:NCP1117-3.3_SOT223 U3
U 1 1 5F615A2F
P 8600 1500
F 0 "U3" H 8600 1742 50  0000 C CNN
F 1 "NCP1117ST33T3G" H 8600 1651 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 8600 1700 50  0001 C CNN
F 3 "http://www.onsemi.com/pub_link/Collateral/NCP1117-D.PDF" H 8700 1250 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Dropout-Regulators-LDO_ON-Semiconductor-ON-NCP1117ST33T3G_C26537.html" H 8600 1500 50  0001 C CNN "LCSC Url"
F 5 "NCP1117ST33T3G" H 8600 1500 50  0001 C CNN "MPN"
	1    8600 1500
	1    0    0    -1  
$EndComp
$Comp
L Device:R R10
U 1 1 5F618C4D
P 7400 1750
F 0 "R10" H 7330 1704 50  0000 R CNN
F 1 "2k" H 7330 1795 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 7330 1750 50  0001 C CNN
F 3 "~" H 7400 1750 50  0001 C CNN
	1    7400 1750
	-1   0    0    1   
$EndComp
$Comp
L Device:LED D16
U 1 1 5F6194EC
P 7400 2050
F 0 "D16" V 7439 1932 50  0000 R CNN
F 1 "Red" V 7348 1932 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 7400 2050 50  0001 C CNN
F 3 "~" H 7400 2050 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Others_TOGIALED-TJ-S1206R-01_C192674.html" H 7400 2050 50  0001 C CNN "LCSC Url"
F 5 "TJ-S3216SW9TGLC2R-A5" H 7400 2050 50  0001 C CNN "MPN"
	1    7400 2050
	0    -1   -1   0   
$EndComp
$Comp
L Device:C C7
U 1 1 5F61A78E
P 7850 1750
F 0 "C7" H 7965 1796 50  0000 L CNN
F 1 "10uF" H 7965 1705 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 7888 1600 50  0001 C CNN
F 3 "~" H 7850 1750 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_Samsung-Electro-Mechanics-CL31F106ZPENNNE_C87993.html" H 7850 1750 50  0001 C CNN "LCSC Url"
F 5 "CL31F106ZPENNNE" H 7850 1750 50  0001 C CNN "MPN"
	1    7850 1750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR028
U 1 1 5F61C41C
P 7650 2500
F 0 "#PWR028" H 7650 2250 50  0001 C CNN
F 1 "GND" H 7655 2327 50  0000 C CNN
F 2 "" H 7650 2500 50  0001 C CNN
F 3 "" H 7650 2500 50  0001 C CNN
	1    7650 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	7400 2200 7400 2500
Wire Wire Line
	7400 2500 7650 2500
Wire Wire Line
	7850 1900 7850 2500
Wire Wire Line
	7850 2500 7650 2500
Connection ~ 7650 2500
Wire Wire Line
	8300 1500 7850 1500
Wire Wire Line
	7400 1500 7400 1600
Wire Wire Line
	7850 1500 7850 1600
Connection ~ 7850 1500
Wire Wire Line
	7850 1500 7400 1500
Wire Wire Line
	7200 1500 7400 1500
Connection ~ 7400 1500
Text Label 7200 1500 2    50   ~ 0
usb_v_ext
Wire Wire Line
	8600 2500 7850 2500
Connection ~ 7850 2500
$Comp
L Device:C C8
U 1 1 5F621D7D
P 9650 2200
F 0 "C8" H 9765 2246 50  0000 L CNN
F 1 "22uF" H 9765 2155 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 9688 2050 50  0001 C CNN
F 3 "~" H 9650 2200 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_SAMSUNG_CL31A226MOCLNNC_22uF-226-20-16V_C159758.html" H 9650 2200 50  0001 C CNN "LCSC Url"
F 5 "CL31A226MOCLNNC" H 9650 2200 50  0001 C CNN "MPN"
	1    9650 2200
	1    0    0    -1  
$EndComp
Connection ~ 8600 2500
Wire Wire Line
	9650 2050 9650 1500
Wire Wire Line
	9650 2350 9650 2500
$Comp
L power:+3.3V #PWR031
U 1 1 5F625784
P 9950 1500
F 0 "#PWR031" H 9950 1350 50  0001 C CNN
F 1 "+3.3V" H 9965 1673 50  0000 C CNN
F 2 "" H 9950 1500 50  0001 C CNN
F 3 "" H 9950 1500 50  0001 C CNN
	1    9950 1500
	-1   0    0    1   
$EndComp
Wire Wire Line
	9650 1500 9950 1500
Connection ~ 9650 1500
$Comp
L Transistor_BJT:BC817 Q1
U 1 1 5F62B6BA
P 8800 3200
F 0 "Q1" H 8991 3246 50  0000 L CNN
F 1 "BC817" H 8991 3155 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 9000 3125 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC817.pdf" H 8800 3200 50  0001 L CNN
F 4 "https://lcsc.com/product-detail/Transistors-NPN-PNP_ON-Semiconductor-ON-BC817-25LT1G_C82635.html" H 8800 3200 50  0001 C CNN "LCSC Url"
F 5 "BC817-25LT1G" H 8800 3200 50  0001 C CNN "MPN"
	1    8800 3200
	1    0    0    -1  
$EndComp
$Comp
L Transistor_BJT:BC817 Q2
U 1 1 5F62D460
P 8800 4050
F 0 "Q2" H 8991 4004 50  0000 L CNN
F 1 "BC817" H 8991 4095 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 9000 3975 50  0001 L CIN
F 3 "http://www.fairchildsemi.com/ds/BC/BC817.pdf" H 8800 4050 50  0001 L CNN
F 4 "https://lcsc.com/product-detail/Transistors-NPN-PNP_ON-Semiconductor-ON-BC817-25LT1G_C82635.html" H 8800 4050 50  0001 C CNN "LCSC Url"
F 5 "BC817-25LT1G" H 8800 4050 50  0001 C CNN "MPN"
	1    8800 4050
	1    0    0    1   
$EndComp
$Comp
L Device:R R11
U 1 1 5F62EF35
P 8150 3200
F 0 "R11" V 7943 3200 50  0000 C CNN
F 1 "12k" V 8034 3200 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8080 3200 50  0001 C CNN
F 3 "~" H 8150 3200 50  0001 C CNN
	1    8150 3200
	0    1    1    0   
$EndComp
$Comp
L Device:R R12
U 1 1 5F62F49B
P 8150 4050
F 0 "R12" V 8350 4050 50  0000 C CNN
F 1 "12k" V 8250 4050 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8080 4050 50  0001 C CNN
F 3 "~" H 8150 4050 50  0001 C CNN
	1    8150 4050
	0    1    1    0   
$EndComp
Wire Wire Line
	8900 4250 9250 4250
Wire Wire Line
	8300 3200 8600 3200
Wire Wire Line
	8900 3400 8450 3400
Wire Wire Line
	8450 3400 8450 3800
Wire Wire Line
	8450 3800 8000 3800
Wire Wire Line
	8000 3800 8000 4050
Wire Wire Line
	8900 3850 8900 3600
Wire Wire Line
	8900 3600 8000 3600
Wire Wire Line
	8000 3600 8000 3200
Wire Wire Line
	8300 4050 8600 4050
Wire Wire Line
	8000 4050 7750 4050
Connection ~ 8000 4050
Wire Wire Line
	8000 3200 7750 3200
Connection ~ 8000 3200
Text HLabel 9250 3000 2    50   Input ~ 0
EN
Text HLabel 9250 4250 2    50   Input ~ 0
IO0
Text Label 4500 2550 0    50   ~ 0
DTR
Text Label 7750 3200 2    50   ~ 0
DTR
Text Label 4500 2350 0    50   ~ 0
RTS
Text Label 7750 4050 2    50   ~ 0
RTS
Text Label 4500 2150 0    50   ~ 0
UTXD
Text Label 4500 2250 0    50   ~ 0
URXD
NoConn ~ 4500 2450
NoConn ~ 4500 2650
NoConn ~ 4500 2750
NoConn ~ 4500 2850
$Comp
L Jumper:SolderJumper_2_Bridged JP1
U 1 1 5F643623
P 8100 4850
F 0 "JP1" H 8100 4963 50  0000 C CNN
F 1 "SolderJumper_2_Bridged" H 8100 4964 50  0001 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm" H 8100 4850 50  0001 C CNN
F 3 "~" H 8100 4850 50  0001 C CNN
	1    8100 4850
	1    0    0    -1  
$EndComp
$Comp
L Jumper:SolderJumper_2_Bridged JP2
U 1 1 5F64543E
P 8100 5050
F 0 "JP2" H 8100 5163 50  0000 C CNN
F 1 "SolderJumper_2_Bridged" H 8100 5164 50  0001 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm" H 8100 5050 50  0001 C CNN
F 3 "~" H 8100 5050 50  0001 C CNN
	1    8100 5050
	1    0    0    -1  
$EndComp
$Comp
L Jumper:SolderJumper_2_Bridged JP3
U 1 1 5F6458A6
P 8100 5250
F 0 "JP3" H 8100 5363 50  0000 C CNN
F 1 "SolderJumper_2_Bridged" H 8100 5364 50  0001 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm" H 8100 5250 50  0001 C CNN
F 3 "~" H 8100 5250 50  0001 C CNN
	1    8100 5250
	1    0    0    -1  
$EndComp
$Comp
L Jumper:SolderJumper_2_Bridged JP4
U 1 1 5F645D0E
P 8100 5450
F 0 "JP4" H 8100 5563 50  0000 C CNN
F 1 "SolderJumper_2_Bridged" H 8100 5564 50  0001 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm" H 8100 5450 50  0001 C CNN
F 3 "~" H 8100 5450 50  0001 C CNN
	1    8100 5450
	1    0    0    -1  
$EndComp
Text Label 7950 5450 2    50   ~ 0
DTR
Text Label 7950 5250 2    50   ~ 0
RTS
Text Label 7950 4850 2    50   ~ 0
UTXD
Text Label 7950 5050 2    50   ~ 0
URXD
$Comp
L Connector:Conn_01x06_Male JSerial1
U 1 1 5F648AE2
P 8550 6000
F 0 "JSerial1" V 8450 6000 50  0000 C CNN
F 1 "Conn_01x06_Male" H 8658 6290 50  0001 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Horizontal" H 8550 6000 50  0001 C CNN
F 3 "~" H 8550 6000 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/New-Arrivals_XFCN-PZ254R-11-06P_C492414.html" H 8550 6000 50  0001 C CNN "LCSC Url"
F 5 "PZ254R-11-06P" H 8550 6000 50  0001 C CNN "MPN"
	1    8550 6000
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8250 5450 8450 5450
Wire Wire Line
	8450 5450 8450 5800
Wire Wire Line
	8250 5250 8550 5250
Wire Wire Line
	8550 5250 8550 5800
Wire Wire Line
	8250 5050 8650 5050
Wire Wire Line
	8650 5050 8650 5800
$Comp
L power:+3.3V #PWR030
U 1 1 5F659A59
P 8850 5700
F 0 "#PWR030" H 8850 5550 50  0001 C CNN
F 1 "+3.3V" V 8865 5828 50  0000 L CNN
F 2 "" H 8850 5700 50  0001 C CNN
F 3 "" H 8850 5700 50  0001 C CNN
	1    8850 5700
	0    1    1    0   
$EndComp
Wire Wire Line
	8850 5700 8850 5800
$Comp
L power:GND #PWR029
U 1 1 5F65C58F
P 8350 5700
F 0 "#PWR029" H 8350 5450 50  0001 C CNN
F 1 "GND" V 8350 5500 50  0000 C CNN
F 2 "" H 8350 5700 50  0001 C CNN
F 3 "" H 8350 5700 50  0001 C CNN
	1    8350 5700
	0    1    1    0   
$EndComp
Wire Wire Line
	8350 5700 8350 5800
Text HLabel 9250 4850 2    50   Input ~ 0
ESP_RX
Text HLabel 9250 5050 2    50   Input ~ 0
ESP_TX
Wire Wire Line
	8250 4850 8400 4850
$Comp
L Diode:1N5817 D13
U 1 1 5F6A3DB8
P 2100 1600
F 0 "D13" H 2100 1384 50  0000 C CNN
F 1 "1N5817" H 2100 1475 50  0000 C CNN
F 2 "Diode_SMD:D_SMB_Handsoldering" H 2100 1425 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88525/1n5817.pdf" H 2100 1600 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Schottky-Barrier-Diodes-SBD_ON-Semiconductor-ON-MBRS260T3G_C45363.html" H 2100 1600 50  0001 C CNN "LCSC Url"
F 5 "" H 2100 1600 50  0001 C CNN "MPN"
	1    2100 1600
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint TP7
U 1 1 5F6B201F
P 7850 1500
F 0 "TP7" H 7908 1572 50  0000 L CNN
F 1 "TestPoint" H 7908 1527 50  0001 L CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 8050 1500 50  0001 C CNN
F 3 "~" H 8050 1500 50  0001 C CNN
	1    7850 1500
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint TP8
U 1 1 5F6B27F8
P 9650 1500
F 0 "TP8" H 9708 1572 50  0000 L CNN
F 1 "TestPoint" H 9708 1527 50  0001 L CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 9850 1500 50  0001 C CNN
F 3 "~" H 9850 1500 50  0001 C CNN
	1    9650 1500
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint TP5
U 1 1 5F6B398A
P 2500 2150
F 0 "TP5" H 2558 2222 50  0000 L CNN
F 1 "TestPoint" H 2558 2177 50  0001 L CNN
F 2 "TestPoint:TestPoint_THTPad_2.0x2.0mm_Drill1.0mm" H 2700 2150 50  0001 C CNN
F 3 "~" H 2700 2150 50  0001 C CNN
	1    2500 2150
	1    0    0    -1  
$EndComp
Connection ~ 2500 2150
$Comp
L Connector:Conn_01x06_Male USB3
U 1 1 5F6B82B1
P 1100 4250
F 0 "USB3" H 1100 4550 50  0000 C CNN
F 1 "USB_PCBhorizontal" H 1800 4550 50  0000 C CNN
F 2 "Connector_USB:USB_Micro-B_Molex_47346-0001" H 1100 4250 50  0001 C CNN
F 3 "~" H 1100 4250 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/USB-Connectors_MOLEX_47346-0001_47346-0001_C132560.html" H 1100 4250 50  0001 C CNN "LCSC Url"
	1    1100 4250
	1    0    0    -1  
$EndComp
Text Label 1300 4050 0    50   ~ 0
usb_v+
Text Label 1300 4250 0    50   ~ 0
usb_d+
Text Label 1300 4150 0    50   ~ 0
usb_d-
$Comp
L power:GND #PWR022
U 1 1 5F6B82BA
P 1550 4450
F 0 "#PWR022" H 1550 4200 50  0001 C CNN
F 1 "GND" H 1555 4277 50  0000 C CNN
F 2 "" H 1550 4450 50  0001 C CNN
F 3 "" H 1550 4450 50  0001 C CNN
	1    1550 4450
	1    0    0    -1  
$EndComp
Wire Notes Line
	2250 4850 2250 2900
Wire Notes Line
	2250 2900 800  2900
Wire Notes Line
	800  2900 800  4850
Wire Notes Line
	800  4850 2250 4850
Text Notes 900  5050 0    50   ~ 0
Alternate USB Connectors, \nonly one to be populated\n
$Comp
L Device:R R13
U 1 1 5F6D3193
P 8550 4850
F 0 "R13" V 8343 4850 50  0000 C CNN
F 1 "470R" V 8434 4850 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8480 4850 50  0001 C CNN
F 3 "~" H 8550 4850 50  0001 C CNN
	1    8550 4850
	0    1    1    0   
$EndComp
Wire Wire Line
	8700 4850 8750 4850
Wire Wire Line
	8900 3000 9250 3000
Wire Wire Line
	8750 4850 9250 4850
Wire Wire Line
	8750 4850 8750 5800
Connection ~ 8750 4850
Wire Wire Line
	8650 5050 9250 5050
Connection ~ 8650 5050
Wire Notes Line
	4650 4500 4650 3300
Wire Notes Line
	4650 3300 5700 3300
Wire Notes Line
	5700 3300 5700 4500
Wire Notes Line
	5700 4500 4650 4500
Text Notes 5350 4500 0    50   ~ 0
optional
Text Notes 8700 2650 0    50   ~ 0
optional: voltage setting
Wire Wire Line
	8600 2500 9650 2500
Wire Wire Line
	8900 1500 9650 1500
Wire Wire Line
	8600 1800 8600 2500
$Comp
L power:+5V #PWR027
U 1 1 5F750605
P 7400 1500
F 0 "#PWR027" H 7400 1350 50  0001 C CNN
F 1 "+5V" H 7415 1673 50  0000 C CNN
F 2 "" H 7400 1500 50  0001 C CNN
F 3 "" H 7400 1500 50  0001 C CNN
	1    7400 1500
	1    0    0    -1  
$EndComp
$Comp
L Connector:Barrel_Jack J5
U 1 1 5F7336E4
P 1000 900
F 0 "J5" H 1057 1225 50  0000 C CNN
F 1 "Barrel_Jack" H 1057 1134 50  0000 C CNN
F 2 "Connector_BarrelJack:BarrelJack_CUI_PJ-063AH_Horizontal" H 1050 860 50  0001 C CNN
F 3 "~" H 1050 860 50  0001 C CNN
F 4 "https://www.digikey.de/product-detail/en/schurter-inc/4840-2201/486-3381-ND/2644239" H 1000 900 50  0001 C CNN "LCSC Url"
	1    1000 900 
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR020
U 1 1 5F734B03
P 1300 1000
F 0 "#PWR020" H 1300 750 50  0001 C CNN
F 1 "GND" H 1305 827 50  0000 C CNN
F 2 "" H 1300 1000 50  0001 C CNN
F 3 "" H 1300 1000 50  0001 C CNN
	1    1300 1000
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N5817 D12
U 1 1 5F73504F
P 2100 800
F 0 "D12" H 2100 584 50  0000 C CNN
F 1 "1N5817" H 2100 675 50  0000 C CNN
F 2 "Diode_SMD:D_SMB_Handsoldering" H 2100 625 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88525/1n5817.pdf" H 2100 800 50  0001 C CNN
F 4 "https://lcsc.com/product-detail/Schottky-Barrier-Diodes-SBD_ON-Semiconductor-ON-MBRS260T3G_C45363.html" H 2100 800 50  0001 C CNN "LCSC Url"
F 5 "" H 2100 800 50  0001 C CNN "MPN"
	1    2100 800 
	-1   0    0    1   
$EndComp
Wire Wire Line
	1300 800  1950 800 
Wire Wire Line
	2250 800  2400 800 
Wire Wire Line
	2400 800  2400 1600
Connection ~ 2400 1600
Wire Wire Line
	1350 3650 1350 3550
Wire Wire Line
	1350 3550 1550 3550
Connection ~ 1350 3550
Wire Wire Line
	1300 4550 1300 4450
Wire Wire Line
	1300 4450 1550 4450
Connection ~ 1300 4450
NoConn ~ 1300 4350
NoConn ~ 1350 3450
Wire Wire Line
	2400 1600 3800 1600
$Comp
L GenericEPaperRemote-rescue:OSS-logo-Codingfragments_common LOGO1
U 1 1 5FAE0DC1
P 1150 7350
F 0 "LOGO1" H 1428 7421 50  0000 L CNN
F 1 "Codingfragments" H 1428 7330 50  0000 L CNN
F 2 "codingfragment-components:OSSLogo" H 1150 7350 50  0001 C CNN
F 3 "" H 1150 7350 50  0001 C CNN
	1    1150 7350
	1    0    0    -1  
$EndComp
$EndSCHEMATC
