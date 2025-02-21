
# Aurora Sofle V2 rev1
The Aurora Sofle v2 is a redesign by splitkb.com of the popular Sofle v2 keyboard by Josef Adamčík.

Keyboard Maintainer: [splitkb.com](https://github.com/splitkb)  
Hardware Supported: Liatris Microcontroller

## Assembly
A build guide for the entire Aurora series is available at [docs.splitkb.com](https://docs.splitkb.com).

## Features
The Aurora Sofle v2 supports the following features:

A comfortable layout with 58 keys, including a number row;
Powered by QMK or ZMK firmware;
Support for MX (see remarks) or Kailh Choc (v1 sold at splitkb.com, not v2) switches;
MX spacing for all variants;
Top mounted controllers for a lower profile;
Up to two 128×32 pixel OLED displays;
One EC11 rotary encoder per half;
Per-key RGB backlight by individual RGB LEDs;
Underglow by individual RGB LEDs;
Support for a power switch for wireless controllers;
Support for the splitkb.com tenting puck.


## What is the Aurora Series?

The Aurora series keyboards are based on the open source keyboard kits from the community. 
Splitkb adds extra functionality like RGB lighting and tenting options while offering good support and documentation.



## CircuitPython to Liatris Microcontroller to PCB Mapping

| circuitpython    | uC Module | kb sch left | kb sch right | 
| ------------     | --------- | ----------- | ------------ |
| GPIO0/D0/TX      | 0/D3/SDA0 |             |              |
| GPIO1/D1/RX      | 1/D2/SCL0 |             |              |
| GPIO2/D2/SDA     | 2/D1/SDA1 | 5/SDA/D1    | 5/SDA/D1     |
| GPIO3/D3/SCL     | 3/D0/SCL1 | 6/SCL/D0    | 6/SCL/D0     |
| GPIO4/D4         | 4/D4      | 7/COL0/D4   | 7/COL4/D4    |
| GPIO5/D5         | 5/C6      | 8/COL1/C6   | 8/COL5/C6    |
| GPIO6/D6         | 6/D7      | 9/COL2/D7   | 9/COL0/D7    |
| GPIO7/D7         | 7/E6      | 10/COL3/E6  | 10/COL1/E6   |
| GPIO8/D8         | 8/B4      | 11/COL4/B4  | 11/COL2/B4   |
| GPIO9/D9         | 9/B5      | 12/COL5/B5  | 12/COL3/B5   |
| GPIO20/D20       | 20/B3     | 15/ROW4/B3  | 15/ROW0/B3   |
| GPIO21/D21       | 21/B6     | 13/ENC1_B/B6| 13/ENCB/B6   |
| GPIO22/D22       | 22/B1     | 16/ROW1/B1  | 16/ROW1/B1   |
| GPIO23/D23       | 23/B2     | 14/ENC1_A/B2| 14/ENCA/B2   |
| GPIO24/POWER_LED | 24/LED    |             |              |
| GPIO25/NEOPIXEL  | 25/RGB    | 1/RGB/D3    | 1/RGB/D3     |
| GPIO26/D26/A0    | 26/F7     | 17/ROW2/F7  | 17/ROW2/F7   |
| GPIO27/D27/A1    | 27/F6     | 18/ROW3/F6  | 18/ROW3/F6   |
| GPIO28/D28/A2    | 28/F5     | 19/ROW0/F5  | 19/ROW4/F5   |
| GPIO29/D29/A3    | 29/F4     | 20/VCC/F4   | 20/GND/F4    |
| GPIO29/D29/A3    | 29/F4     | 20/VCC/F4   | 20/GND/F4    |


Readout from REPL

```python
import board
print(dir(board))
['__class__', '__name__', 'A0', 'A1', 'A2', 'A3', 'D0', 'D1', 'D12', 'D13', 'D14', 'D15', 'D16', 'D2', 'D20', 'D21', 'D22', 'D23', 'D26', 'D27', 'D28', 'D29', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'I2C', 'MISO', 'MOSI', 'NEOPIXEL', 'POWER_LED', 'RX', 'SCK', 'SCL', 'SDA', 'SPI', 'TX', 'UART', 'VBUS_SENSE', '__dict__', 'board_id']
```
