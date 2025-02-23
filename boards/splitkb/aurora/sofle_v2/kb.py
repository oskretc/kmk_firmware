from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.split import SplitSide
from kmk.quickpin.pro_micro.liatris import pinout as pins
from kmk.scanners import DiodeOrientation
import board
side = SplitSide.LEFT if str(getmount('/').label)[-1] == 'L' else SplitSide.RIGHT

# With normal col/row mapping, my Left COL1 buttons kept triggering despite it being a working board.
# When swapping cols and rows (and diode_orientation to match) it's working as expected though.
# The coord_mapping corrects the colums for rows change so the other code remains unaffected.


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        self.col_pins = (
            (board.D6, board.D7, board.D8, board.D9, board.D4, board.D5)
            if side == SplitSide.LEFT
            else (board.D4, board.D5, board.D6, board.D7, board.D8, board.D9)
        )
        self.row_pins = (
            (board.D20, board.D22, board.D26, board.D27, board.D28)
            if side == SplitSide.LEFT
            else (board.D28, board.D22, board.D26, board.D27, board.D20)
        )
        self.diode_orientation = DiodeOrientation.COL2ROW
        self.data_pin = board.D1
        self.rgb_pixel_pin = board.D0
        self.SCL = board.SCL
        self.SDA = board.SDA
        self.power_led = board.POWER_LED
        self.side = side
        

        # fmt:off
        self.coord_mapping = [
             27,  26, 25, 24, 29, 28,           56, 57, 58, 59, 54, 55,
              9,   8,  7,  6, 11, 10,           38, 39, 40, 41, 36, 37,
             15,  14, 13, 12, 17, 16,           44, 45, 46, 47, 42, 43,
             21,  20, 19, 18, 23, 22,           50, 51, 52, 53, 48, 49,
                       3,  2,  1, 0,  5,    33, 34, 35, 30,31
        ]
        self.led_key_pos = [
            11,10,9 ,8 ,7 ,6 ,       41,42,43,44,45,46,
            12,13,14,15,16,17,       52,51,50,49,48,47,
            23,22,21,20,19,18,       53,54,55,56,57,58,
            24,25,26,27,28,29,30, 65,64,63,62,61,60,59,
                     34,33,32,31, 66,67,68,69,
                     3 ,4 ,5 ,       40,39,38,
                     2 ,1 ,0 ,       35,36,37
        ]
        self.brightness_limit = 1.0
        self.num_pixels = 35

        # fmt:on
