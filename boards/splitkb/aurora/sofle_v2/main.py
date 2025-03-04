from kb import KMKKeyboard

from kmk.extensions.display import Display, TextEntry,ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split,SplitType,SplitSide
from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color
from kmk.extensions.LED import LED
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode,ScrollDirection,ScrollHandler, PointingHandler, KeyHandler
from kmk.modules.mouse_keys import MouseKeys
import busio as io
from kmk.modules.combos import Combos, Chord, Sequence
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
combo_layers = {(1, 2): 3}
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
# rgb = RGB(
#     pixel_pin=keyboard.rgb_pixel_pin,
#     num_pixels=35,
#     hue_default=128,
#     sat_default=255,
#     val_default=4
# )
ALPHA = Color.AZURE
MODS = Color.ORANGE
LAYER= Color.RED
NUMS = Color.CYAN

rgb = Rgb_matrix(ledDisplay=Rgb_matrix_data(
    keys=[
    MODS,NUMS,NUMS,NUMS,NUMS,NUMS,                        NUMS,NUMS,NUMS,NUMS,NUMS,MODS,
    MODS,ALPHA,ALPHA,ALPHA,ALPHA,ALPHA,                        ALPHA,ALPHA,ALPHA,ALPHA,ALPHA,MODS,
    MODS,ALPHA,ALPHA,ALPHA,ALPHA,ALPHA,                        ALPHA,ALPHA,ALPHA,ALPHA,ALPHA,MODS,
    MODS,ALPHA,ALPHA,ALPHA,ALPHA,ALPHA,                        ALPHA,ALPHA,ALPHA,ALPHA,ALPHA,MODS,
                          MODS,MODS,LAYER,LAYER,MODS,  MODS,LAYER,MODS,MODS,MODS],
                                    
    underglow=[ 
             [0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55]]
             ),
    split=True,
    rightSide=True,
    disable_auto_write=True)




i2c_bus = io.I2C(sda=keyboard.SDA, scl=keyboard.SCL)
display_driver = SSD1306(
    i2c=i2c_bus,
    # Optional device_addres argument. Default is 0x3C.
    # device_address=0x3C,
)    

display = Display(
    display=display_driver,
    entries=[
        # TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
        # TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
        # TextEntry(text='SYM', x=40, y=32, y_anchor='B', layer=1),
        # TextEntry(text='NAV', x=40, y=32, y_anchor='B', layer=2),
        # TextEntry(text='ADJ', x=40, y=32, y_anchor='B', layer=3),
        # TextEntry(text='I3', x=40, y=32, y_anchor='B', layer=4),
        # TextEntry(text='0 1 2 3 4', x=0, y=4),
        # TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        # TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
        # TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
        # TextEntry(text='3', x=36, y=4, inverted=True, layer=3),
        # TextEntry(text='4', x=48, y=4, inverted=True, layer=4),
        ImageEntry(image="0.bmp", x=0, y=0, layer=0),
        ImageEntry(image="1.bmp", x=0, y=0, layer=1),
        ImageEntry(image="2.bmp", x=0, y=0, layer=2),
        ImageEntry(image="3.bmp", x=0, y=0, layer=3),
        ImageEntry(image="4.bmp", x=0, y=0, layer=4),
    ],
    dim_time=10,
    dim_target=0.1,
    off_time=1200,
    brightness=1,
    flip_right=True
)

if keyboard.side==SplitSide.RIGHT:
    trackball = Trackball(
        i2c_bus,
        angle_offset=270,
        mode=TrackballMode.SCROLL_MODE,
        handlers=[
            KeyHandler(KC.UP, KC.RIGHT, KC.DOWN, KC.LEFT, KC.ENTER),
            PointingHandler(on_press=KC.MB_LMB),
            # use ScrollDirection.NATURAL (default) or REVERSE to change the scrolling direction, left click when pressed
            ScrollHandler(scroll_direction=ScrollDirection.REVERSE, on_press=KC.MB_LMB)
        ]
    )
    trackball.set_blue(50)
    keyboard.modules.append(trackball)

keyboard.extensions = [leds,rgb, display, MediaKeys()]

mousekeys = MouseKeys(
    max_speed = 10,
    acc_interval = 20, # Delta ms to apply acceleration
    move_step = 1
)

keyboard.modules.append(mousekeys)

from kmk.modules.macros import Macros

macros = Macros()
keyboard.modules.append(macros)


combos = Combos()
keyboard.modules.append(combos)

combos.combos = [
    Chord((KC.J, KC.F), KC.ESC, timeout=500, per_key_timeout=False)
]

import keymap as keymap

keyboard.keymap= keymap.KEYMAP

if __name__ == '__main__':
    keyboard.go()
