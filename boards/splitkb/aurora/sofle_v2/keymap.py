from kmk.keys import KC
from kmk.modules.mouse_keys import MouseKeys

from kmk.modules.split import SplitSide
from storage import getmount
side = SplitSide.LEFT if str(getmount('/').label)[-1] == 'L' else SplitSide.RIGHT
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

ENTER = KC.HT(KC.ENT, KC.LCTRL)
LOWER = KC.MO(1)
# BSPC = KC.LT(2, KC.BSPC)
BSPC = KC.BSPC
UPPER = KC.MO(2)
# ADJUST = KC.MO(3)
ADJR = KC.LT(3, KC.QUOT)
ADJL = KC.LT(3, KC.ESC)
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

ZEUP =KC.LCTL(KC.UP)
ZEDN =KC.LCTL(KC.DOWN)
ZELF =KC.LCTL(KC.LEFT)
ZERT =KC.LCTL(KC.RIGHT)

# I3
FOLFT = KC.LGUI(KC.LEFT)
FORGH = KC.LGUI(KC.RIGHT)
SWTDES = KC.LGUI(KC.D)
FO1 = KC.LGUI(KC.N1)
FO2 = KC.LGUI(KC.N2)
FO3 = KC.LGUI(KC.N3)
FO4 = KC.LGUI(KC.N4)
FO5 = KC.LGUI(KC.N5)
if side==SplitSide.RIGHT:
    M_KEYS=KC.TB_HANDLER(0)
    M_POINT=KC.TB_HANDLER(1)
    M_SCROL=KC.TB_HANDLER(2)
    M_LMB = KC.MB_LMB
else:
    M_KEYS= XXXXXXX
    M_POINT=XXXXXXX
    M_SCROL=XXXXXXX
    M_LMB = XXXXXXX

import secrets as secrets

P1 = KC.MACRO(secrets.P1)
P2 = KC.MACRO(secrets.P2)
# fmt:off
KEYMAP = [
    [  #QWERTY
        ADJL   , KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                          KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   BSPC,
        KC.TAB , KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                           KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.DEL,
        KC.LSFT, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                           KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, ADJR,
        KC.LCTL, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                           KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,
                          KC.LGUI, KC.LALT, I3GUI  , LOWER  , ENTER  ,      KC.SPC , UPPER  , KC.RCTL, KC.RALT, KC.UNDS,

    ],
    [   #LOWER
        XXXXXXX, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,                          KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.PLUS,                        M_LMB  , KC.UNDS, XXXXXXX, XXXXXXX, XXXXXXX, KC.F12,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.EQL,                         LPAR   , RPAR   , XXXXXXX, XXXXXXX, XXXXXXX, KC.PIPE,
        _______, KC.EQL , KC.MINS, KC.PLUS, KC.LCBR, KC.RCBR,                        KC.LBRC, KC.RBRC, XXXXXXX, XXXXXXX, KC.BSLS, XXXXXXX,
                          _______, _______, _______, _______, _______,      _______, _______, _______, _______,_______,
    ],
    [   #UPPER
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        MENU,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, P1,
        XXXXXXX, XXXXXXX, ZEUP   , XXXXXXX, XXXXXXX, XXXXXXX,                        KC.VOLU, KC.HOME, KC.UP,   KC.END,  KC.PGUP, P2,
        _______, ZELF   , ZEDN   , ZERT   , XXXXXXX, XXXXXXX,                        KC.VOLD, KC.LEFT, KC.DOWN, KC.RGHT, KC.PGDN, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.MPLY, KC.INS,  KC.DEL,  XXXXXXX, XXXXXXX, XXXXXXX,
                          _______, _______, _______, _______, _______,      _______, _______, _______, _______,_______,
    ],
    [   #ADJUST
        XXXXXXX, RGB1   , RGB2   , RGB3   , RGB4   , RGB5   ,                        RGB1,    RGB2,    RGB3,    RGB4,    RGB5,    RGB6,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        M_KEYS , XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, PWRLEDTOG,
        _______, XXXXXXX, PWRLEDTOG, XXXXXXX, XXXXXXX, XXXXXXX,                      M_POINT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, RGBTOG,
        _______, XXXXXXX, RGBTOG , XXXXXXX, XXXXXXX, XXXXXXX,                        M_SCROL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
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
