from kb import KMKKeyboard

from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split,SplitType,SplitSide
# from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color
from kmk.extensions.LED import LED
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode,ScrollDirection,ScrollHandler, PointingHandler, KeyHandler
import busio as io

keyboard = KMKKeyboard()

# Adding modules
# Using drive names (LILY58L, LILY58R) to recognize sides; use split_side arg if you're not doing it
split = Split(
    split_target_left=False,
    split_type=SplitType.UART,
    split_flip=False,
    # data_pin=keyboard.data_pin,
    use_pio=True,
)
combo_layers = {(2, 1): 3}
layers = Layers(combo_layers)
keyboard.modules = [split, layers, HoldTap()]


# POWER LED CONTROL
# leave it at min brightness
leds = LED(
    led_pin=[keyboard.power_led],
    brightness = 99
    
)


# Adding extensions
# **RGB requires neopixel.py library to work**
#
rgb = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=35,
    hue_default=128,
    sat_default=255,
    val_default=4
)

i2c_bus = io.I2C(sda=keyboard.SDA, scl=keyboard.SCL)
display_driver = SSD1306(
    i2c=i2c_bus,
    # Optional device_addres argument. Default is 0x3C.
    # device_address=0x3C,
)    

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
        TextEntry(text='SYM', x=40, y=32, y_anchor='B', layer=1),
        TextEntry(text='NAV', x=40, y=32, y_anchor='B', layer=2),
        TextEntry(text='ADJ', x=40, y=32, y_anchor='B', layer=3),
        TextEntry(text='I3', x=40, y=32, y_anchor='B', layer=4),
        TextEntry(text='0 1 2 3 4', x=0, y=4),
        TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
        TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
        TextEntry(text='3', x=36, y=4, inverted=True, layer=3),
        TextEntry(text='4', x=48, y=4, inverted=True, layer=4),
    ],
    dim_time=10,
    dim_target=0.1,
    off_time=1200,
    brightness=1,
    flip_right=True
)

keyboard.extensions = [leds,rgb, display, MediaKeys()]

if keyboard.side==SplitSide.RIGHT:
    trackball = Trackball(
        i2c_bus,
        angle_offset=270,
        mode=TrackballMode.SCROLL_MODE,
        handlers=[
            KeyHandler(KC.UP, KC.RIGHT, KC.DOWN, KC.LEFT, KC.ENTER),
            PointingHandler(),
            # use ScrollDirection.NATURAL (default) or REVERSE to change the scrolling direction, left click when pressed
            ScrollHandler(scroll_direction=ScrollDirection.REVERSE, on_press=KC.MB_LMB)
        ]
    )
    trackball.set_blue(50)
    keyboard.modules.append(trackball)


# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

ENTER = KC.HT(KC.ENT, KC.LCTRL)
LOWER = KC.MO(1)
# BSPC = KC.LT(2, KC.BSPC)
BSPC = KC.BSPC
UPPER = KC.MO(2)
# ADJUST = KC.MO(3)
ADJR = KC.LT(3, KC.RSFT)
ADJL = KC.LT(3, KC.LALT)
I3GUI = KC.LT(4, KC.LGUI)

# Symbols
LPAR = KC.LSFT(KC.N9)
RPAR = KC.LSFT(KC.N0)
LGT = KC.LSFT(KC.COMM)
RGT = KC.LSFT(KC.DOT)
PIPE = KC.LSFT(KC.BSLS)
AMP = KC.LSFT(KC.N7)
EUR = KC.RALT(KC.N5)

# Media/Nav/Other
MENU = KC.LGUI(KC.F12)

# RGB
RGB1 = KC.RGB_M_P
RGB2 = KC.RGB_M_B
RGB3 = KC.RGB_M_R
RGB4 = KC.RGB_M_BR
RGB5 = KC.RGB_M_K
RGB6 = KC.RGB_M_S
RGBTOG = KC.RGB_TOG

PWRLEDTOG = KC.LED_INC(0)

# I3
FOLFT = KC.LGUI(KC.LEFT)
FORGH = KC.LGUI(KC.RIGHT)
SWTDES = KC.LGUI(KC.D)
FO1 = KC.LGUI(KC.N1)
FO2 = KC.LGUI(KC.N2)
FO3 = KC.LGUI(KC.N3)
FO4 = KC.LGUI(KC.N4)
FO5 = KC.LGUI(KC.N5)
# fmt:off
keyboard.keymap = [
    [  #QWERTY
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                          KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   BSPC,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                           KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.DEL,
        KC.LSFT, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                           KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.LCTL, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                           KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, ADJR,
                          KC.LGUI, ADJL, I3GUI  , LOWER  , ENTER  ,      KC.SPC , UPPER  , KC.RCTL, KC.RALT, KC.UNDS,

    ],
    [   #LOWER
        XXXXXXX, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,                          KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.PLUS,                        XXXXXXX, KC.UNDS, XXXXXXX, XXXXXXX, XXXXXXX, KC.F12,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.EQL,                         LPAR   , RPAR   , XXXXXXX, XXXXXXX, XXXXXXX, KC.PIPE,
        _______, KC.EQL , KC.MINS, KC.PLUS, KC.LCBR, KC.RCBR,                        KC.LBRC, KC.RBRC, XXXXXXX, XXXXXXX, KC.BSLS, XXXXXXX,
                          _______, _______, _______, _______, _______,      _______, _______, _______, _______,_______,
    ],
    [   #UPPER
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        MENU,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.VOLU, KC.HOME, KC.UP,   KC.END,  KC.PGUP, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.VOLD, KC.LEFT, KC.DOWN, KC.RGHT, KC.PGDN, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.MPLY, KC.INS,  KC.DEL,  XXXXXXX, XXXXXXX, XXXXXXX,
                          _______, _______, _______, _______, _______,      _______, _______, _______, _______,_______,
    ],
    [   #ADJUST
        XXXXXXX, RGB1   , RGB2   , RGB3   , RGB4   , RGB5   ,                        RGB1,    RGB2,    RGB3,    RGB4,    RGB5,    RGB6,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.TB_NEXT_HANDLER, PWRLEDTOG,
        _______, XXXXXXX, PWRLEDTOG, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, RGBTOG,
        _______, XXXXXXX, RGBTOG , XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                          _______, _______, _______, _______, _______,      _______, _______, _______, _______,_______,
    ],
    [   #I3
        XXXXXXX, FO1    , FO2    , FO3    , FO4    , FO5    ,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, KC.UP  , XXXXXXX, XXXXXXX, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, SWTDES , XXXXXXX, XXXXXXX,                        XXXXXXX, FOLFT  , KC.DOWN, FORGH  , XXXXXXX, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                          _______, _______, _______, _______, _______,      _______, _______, _______, _______,_______,
    ]
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
