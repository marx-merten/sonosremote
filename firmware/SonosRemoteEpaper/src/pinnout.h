

// ESP32 nodeMCU 32S
//                                   +------------------------------+
//                          VIN/3V3 -|                              |- GND
//                        RESET--EN -|                [  disp_din  ]|- GPIO23--VPSIMOSI
// (I Only)           ADC0---GPIO36 -| [ in0        ] [ disp_dc    ]|- GPIO22--I2C SCL
// (I Only)           ADC3---GPIO39 -| [ in1        ] [            ]|- GPIO1---TX0
// (I Only)           ADC6---GPIO34 -| [ in2        ] [            ]|- GPIO3---RX0
// (I Only)           ADC7---GPIO35 -| [ in3        ] [ disp_rst   ]|- GPIO21--I2C SDA
//            Touch9--ADC4---GPIO32 -| [ sel0       ]               |- GND
//            Touch8--ADC5---GPIO33 -| [ sel1       ] [            ]|- GPIO19--VSPIMISO
//              DAC1--ADC18--GPIO25 -| [ sel2       ] [ disp_clk   ]|- GPIO18--VSPI/SCK
//              DAC2--ADC19--GPIO26 -| [ speaker    ] [ disp_cs    ]|- GPIO5---VSPI/SS
//            Touch7--ADC17--GPIO27 -| [ rot_b      ] [ *PS-Ram*   ]|- GPIO17--TX1
//  HSPI/CLK--Touch6--ADC16--GPIO14 -| [*jtag*      ] [ *PS-Ram*   ]|- GPIO16--RX1
//  HSPIMISO--Touch5--ADC15--GPIO12 -| [*jtag*      ] [ disp_busy  ]|- GPIO4---ADC10----TOUCH0
//                              GND -| [            ] [ rot_a      ]|- GPIO0---ADC11----TOUCH1
//  HSPIMOSI--Touch4--ADC14--GPIO13 -| [*jtag*      ] [ (neopixel) ]|- GPIO2---ADC12----TOUCH2
//                 FLASH/D2---GPIO9 -| [**reserved**] [ **jtag**   ]|- GPIO15--ADC13----TOUCH3--HSPI/CS
//                 FLASH/D3--GPIO10 -| [**reserved**] [**reserved**]|- GPIO8---FLASH/D1
//                 FLASHCMD--GPIO11 -| [**reserved**] [**reserved**]|- GPIO7---FLASH/D0
//                           VIN/5V -|                [**reserved**]|- GPIO6---FLASHSCK
//                                   +------------+-----+-----------+
//                                      (EN)     | USB |  (Prog)
//                                              +-----+
//<JTAG PINS>

// Used Pins
