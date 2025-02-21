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
        self.rgb_pixel_pin = board.NEOPIXEL
        self.SCL = board.SCL
        self.SDA = board.SDA

        # fmt:off
        self.coord_mapping = [
             27,  26, 25, 24, 29, 28,           30, 35, 40, 45, 50, 55,
             9,  8, 7, 6, 11, 10,           31, 36, 41, 46, 51, 56,
             15,  14, 13, 12, 17, 16,           32, 37, 42, 47, 52, 57,
             21,  20, 19, 18, 23, 22,  9,   54, 33, 38, 43, 48, 53, 58,
                        3, 2, 1, 0, 5,    34, 39, 44, 49
        ]
        # fmt:on
