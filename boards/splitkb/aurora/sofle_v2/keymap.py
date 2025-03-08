from kmk.keys import KC,Key
import time

from kmk.modules.split import SplitSide
from storage import getmount

side = SplitSide.LEFT if str(getmount('/').label)[-1] == 'L' else SplitSide.RIGHT

class CTHOMEKey(Key):
    def __init__(self):
        pass
    def on_press(self, keyboard, coord_int=None):
        keyboard.add_key(KC.LCTL)
        time.sleep(0.1)
        keyboard.add_key(KC.LALT)
        time.sleep(0.1)
        keyboard.add_key(KC.HOME)
        time.sleep(0.1)
        
        
    def on_release(self, keyboard, coord_int=None):
        keyboard.remove_key(KC.HOME)
        time.sleep(0.1)
        keyboard.remove_key(KC.LALT)
        time.sleep(0.1)
        keyboard.remove_key(KC.LCTL)
        time.sleep(0.1)
        
KC_RDPE = KC.NO
    
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

ENTER = KC.HT(KC.ENT, KC.LCTRL)
SPACE = KC.HT(KC.SPC, KC.RSFT)
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
# RGB1 = KC.RGB_M_P
RGB1 = KC.RGB_BRI
# RGB2 = KC.RGB_M_B
RGB2 = KC.RGB_BRD
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
FOUP = KC.LGUI(KC.UP)
FODN = KC.LGUI(KC.DOWN)
SWTDES = KC.LGUI(KC.D)
FO1 = KC.LGUI(KC.N1)
FO2 = KC.LGUI(KC.N2)
FO3 = KC.LGUI(KC.N3)
FO4 = KC.LGUI(KC.N4)
FO5 = KC.LGUI(KC.N5)
MWSL= KC.LGUI(KC.LSFT(KC.A))
MWSR= KC.LGUI(KC.LSFT(KC.F))

LAUNC=KC.RALT(KC.SPC)
WTAB=KC.LGUI(KC.TAB)
CTAB=KC.LCTL(KC.TAB)
CSTAB=KC.LCTL(KC.LSFT(KC.TAB))
CAHOM=KC.RCTL(KC.RALT(KC.HOME))


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
        ADJL   , KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                          KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.DEL,
        KC.TAB , KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                           KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    BSPC,
        KC.LSFT, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                           KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, ADJR,
        KC.LCTL, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                           KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,
                          KC.LGUI, KC.LALT, I3GUI  , LOWER  , ENTER  ,      SPACE , UPPER  , KC.RCTL, KC.RALT, KC.RGUI,

    ],
    [   #LOWER
        XXXXXXX, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,                          KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
        XXXXXXX, KC.TILDE, KC.GRV, XXXXXXX, KC.PLUS, KC.MINS,                        M_LMB  , KC.UNDS, XXXXXXX, XXXXXXX, XXXXXXX, KC.F12,
        _______, KC.AT  , XXXXXXX, XXXXXXX, XXXXXXX, KC.EQL,                         LPAR   , RPAR   , XXXXXXX, XXXXXXX, XXXXXXX, KC.PIPE,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, KC.LCBR, KC.RCBR,                        KC.LBRC, KC.RBRC, XXXXXXX, XXXXXXX, KC.BSLS, XXXXXXX,
                          _______, _______, _______, _______, _______,      LAUNC  , _______, _______, _______,_______,
    ],
    [   #UPPER
        XXXXXXX, FO1    , FO2    , FO3    , FO4    , FO5    ,                        MENU,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, P1,
        XXXXXXX, XXXXXXX, ZEUP   , XXXXXXX, CSTAB  , CTAB   ,                        KC.VOLU, KC.HOME, XXXXXXX,   KC.END,  KC.PGUP, P2,
        _______, ZELF   , ZEDN   , ZERT   , CAHOM, KC_RDPE  ,                        KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.PGDN, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, MWSL   , MWSR   ,                        KC.MPLY, KC.INS,  KC.DEL,  XXXXXXX, XXXXXXX, XXXXXXX,
                          _______, _______, _______, _______, WTAB   ,      _______, _______, _______, _______,_______,
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
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, SWTDES , XXXXXXX, XXXXXXX,                        FOLFT  , FODN   , FOUP   , FORGH  , XXXXXXX, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, MWSL   , MWSR   ,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                          XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,XXXXXXX,
    ]
]


# Mod-taps
A_SFT = KC.HT(KC.A, KC.LSFT)
SCLN_SFT = KC.HT(KC.SCLN, KC.LSFT)
X_CTL = KC.HT(KC.X, KC.LCTRL)
C_ALT = KC.HT(KC.C, KC.LALT)
COM_ALT = KC.HT(KC.COMM, KC.LALT)
DOT_CTL = KC.HT(KC.DOT, KC.LCTRL)
CTL_ALT = KC.LCTRL(KC.LALT)


# Layer tap for other home row keys
S_L5 = KC.LT(5, KC.S)
D_L1 = KC.LT(1, KC.D)
F_L3 = KC.LT(3, KC.F)
J_L4 = KC.LT(4, KC.J)
K_L2 = KC.LT(2, KC.K)
L_L6 = KC.LT(6, KC.L)
SPC_L7 = KC.LT(7, KC.SPC)

# fmt: off
KEYMAP_FERRIS = [
    [  # QWERTY
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, KC.Q   , KC.W   , KC.E   , KC.R   , KC.T   ,                        KC.Y   , KC.U   , KC.I   , KC.O   , KC.P   , XXXXXXX,
        XXXXXXX, A_SFT  , S_L5   , D_L1   , F_L3   , KC.G   ,                        KC.H,    J_L4,    K_L2,    L_L6, SCLN_SFT,XXXXXXX,
        XXXXXXX, KC.Z,  X_CTL,  C_ALT,    KC.V,    KC.B,    KC.N,    KC.M, COM_ALT, DOT_CTL,  KC.SLSH,XXXXXXX,
                                XXXXXXX, XXXXXXX, XXXXXXX, KC.LGUI, ENTER,  SPC_L7,  KC.BSPC,XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  # MOUSE
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
       XXXXXXX, _______,   _______, _______,   _______, _______, _______, KC.MB_LMB, KC.MW_UP, KC.MB_LMB,  _______,XXXXXXX,
       XXXXXXX, _______, KC.MB_RMB, _______, KC.MB_LMB, _______, _______,  KC.MS_LT, KC.MS_DN,  KC.MS_UP, KC.MS_RT,XXXXXXX,
       XXXXXXX, _______,   _______, _______,   _______, _______, _______,   _______, KC.MW_DN,   _______,  _______,XXXXXXX,
                                      XXXXXXX, XXXXXXX, XXXXXXX, _______, _______, _______, _______,XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  # NAVIGATION
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,_______, _______, KC.PGUP, _______, _______, _______, _______, _______, _______, _______,XXXXXXX,
        XXXXXXX,KC.LEFT,   KC.UP, KC.DOWN, KC.RGHT, _______, _______, KC.LGUI, CTL_ALT,  KC.MEH, KC.HYPR,XXXXXXX,
        XXXXXXX,_______, KC.HOME, KC.PGDN,  KC.END, _______, _______, _______, _______, _______, _______,XXXXXXX,
                                   XXXXXXX, XXXXXXX, XXXXXXX,_______, _______, _______, _______,XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  # RIGHT SYMBOLS
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,_______, _______, _______, _______, _______, _______, KC.UNDS, KC.PIPE, KC.QUOT, _______,XXXXXXX,
        XXXXXXX,KC.CIRC, KC.ASTR, KC.AMPR, _______, _______, KC.HASH, KC.TILD, KC.SLSH, KC.DQUO,  KC.DLR,XXXXXXX,
        XXXXXXX,_______, _______, _______, _______, _______, _______, KC.MINS, KC.BSLS,  KC.GRV, _______,XXXXXXX,
                                   XXXXXXX, XXXXXXX, XXXXXXX,_______, _______, _______, _______,XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  # LEFT SYMBOLS
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,_______, KC.COLN, KC.LABK, KC.RABK, KC.SCLN, _______, _______, _______, _______, _______,XXXXXXX,
        XXXXXXX,KC.LCBR, KC.RCBR, KC.LPRN, KC.RPRN,   KC.AT, _______, _______,  KC.EQL, KC.PLUS, KC.PERC,XXXXXXX,
        XXXXXXX,_______, KC.EXLM, KC.LBRC, KC.RBRC, _______, _______, _______, _______, _______, _______,XXXXXXX,
                                   XXXXXXX, XXXXXXX, XXXXXXX,_______, _______, _______, _______,XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  # 5 FUNCTION
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,_______, _______, _______, _______, _______, _______, KC.F7, KC.F8, KC.F9, KC.F10,XXXXXXX,
        XXXXXXX,_______, _______, _______, _______, _______, _______, KC.F4, KC.F5, KC.F6, KC.F11,XXXXXXX,
        XXXXXXX,_______, _______, _______, _______, _______, _______, KC.F1, KC.F2, KC.F3, KC.F12,XXXXXXX,
                                   XXXXXXX, XXXXXXX, XXXXXXX,_______, _______, _______, _______,XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  # 6 NUMBERS
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
       XXXXXXX, KC.SLSH,   KC.N7,   KC.N8,   KC.N9, KC.PLUS, _______, _______, _______, _______, _______,XXXXXXX,
         XXXXXXX, KC.N0,   KC.N1,   KC.N2,   KC.N3, KC.MINS, _______, _______, _______, _______, _______,XXXXXXX,
       XXXXXXX, KC.ASTR,   KC.N4,   KC.N5,   KC.N6,  KC.EQL, _______, _______, _______, _______, _______,XXXXXXX,
                                   XXXXXXX, XXXXXXX, XXXXXXX,_______, _______, _______, _______,XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  # 7 ALWAYS AVAILABLE
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,_______, _______, KC.COLN,  KC.ESC, _______, _______, _______, _______, _______,  KC.DEL,XXXXXXX,
        XXXXXXX,_______, KC.PERC, KC.SLSH,  KC.ENT, _______, KC.DF(1), KC.LGUI, _______, _______, _______,XXXXXXX,
        XXXXXXX,_______, _______, _______, KC.PERC, _______, KC.DF(0), KC.RALT, KC.RCTL, _______, KC.RESET,XXXXXXX,
                                   XXXXXXX, XXXXXXX, XXXXXXX,_______,  KC.TAB, KC.LSFT, _______,XXXXXXX, XXXXXXX, XXXXXXX,
    ],
]
# fmt:on
