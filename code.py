print("Starting")


# Importation des modules nécessaires pour le fonctionnement du clavier.
import board  # Importation de la bibliothèque 'board' qui donne accès aux pins et autres fonctionnalités du microcontrôleur.

from kmk.kmk_keyboard import KMKKeyboard  # Importation de la bibliothèque 'board' qui donne accès aux pins et autres fonctionnalités du microcontrôleur.
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.tapdance import TapDance
from kmk.extensions.RGB import RGB
from midi import Midi


# Initialisation et configuration de l'objet clavier.
# KEYTBOARD SETUP
layers = Layers()
keyboard = KMKKeyboard()
encoders = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules = [layers, encoders, tapdance]

# SWITCH MATRIX: Configuration de la matrice de commutation, définissant les pins des colonnes et des rangées.
keyboard.col_pins = (board.D3, board.D4, board.D5, board.D6)
keyboard.row_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ENCODERS: Configuration des encodeurs (rotatifs), qui peuvent être utilisés pour ajuster le volume, changer de chanson, etc.
encoders.pins = ((board.A2, board.A1, board.A0, False), (board.SCK, board.MISO, board.MOSI, False),)

# EXTENSIONS: Ajout d'extensions pour le clavier, telles que les LEDs RGB et la fonctionnalité MIDI.
rgb_ext = RGB(pixel_pin = board.D10, num_pixels=4, hue_default=100)
midi_ext = Midi()
keyboard.extensions.append(rgb_ext)
keyboard.extensions.append(midi_ext)
keyboard.debug_enabled = False

# MACROS ROW 1: Définition des macros, qui sont des séquences de touches programmées pour exécuter des actions spécifiques.
GIT = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('open https://github.com'), KC.ENTER])
G_STATUS = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('git status'), KC.ENTER])
G_PULL = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('git fetch origin'), KC.ENTER])
G_COMMIT = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('git commit -m ""'), KC.LEFT])

# MACROS ROW 2: Définition des macros, qui sont des séquences de touches programmées pour exécuter des actions spécifiques.
BROWSER = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('open https://ocrism.studio'), KC.ENTER])
CLEAR = simple_key_sequence([KC.LCMD(KC.LSFT(KC.BSPC))])
INSPECT = simple_key_sequence([KC.LCMD(KC.LALT(KC.I))])
HARD_RELOAD = simple_key_sequence([KC.LCMD(KC.LSFT(KC.R))])

# MACROS ROW 3: Définition des macros, qui sont des séquences de touches programmées pour exécuter des actions spécifiques.
TERMINAL = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.LCTRL(KC.U)])
FORCE_QUIT = simple_key_sequence([KC.LCMD(KC.LALT(KC.ESCAPE))])
MUTE = KC.MUTE
LOCK = simple_key_sequence([KC.LCTRL(KC.LCMD(KC.Q)), KC.MACRO_SLEEP_MS(400), KC.ESCAPE])


# La constante "_______" représente une touche "transparente". Lorsqu'elle est utilisée dans une couche de clavier,
# elle hérite du comportement de la touche de la même position dans la couche précédente.
# C'est utile pour ne pas avoir à redéfinir chaque touche dans chaque couche.
_______ = KC.TRNS

# La constante "xxxxxxx" représente une touche qui n'a aucune fonction ou action associée.
# Si cette touche est pressée, rien ne se produira.
xxxxxxx = KC.NO


# Configuration du 'tap dance', une fonctionnalité qui permet d'effectuer différentes actions en fonction du nombre de tapotements.
# LAYER SWITCHING TAP DANCE
TD_LYRS = KC.TD(LOCK, KC.MO(1), xxxxxxx, KC.TO(2))
MIDI_OUT = KC.TD(KC.MIDI(70), xxxxxxx, xxxxxxx, KC.TO(0))

# array of default MIDI notes
# midi_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

# Définition des mappages de touches pour chaque couche du clavier.
# KEYMAPS

keyboard.keymap = [
    # MACROS
    [
        TERMINAL,   FORCE_QUIT,     KC.MUTE,    TD_LYRS,
        BROWSER,    CLEAR,          INSPECT,    HARD_RELOAD,
        GIT,    G_STATUS,       G_PULL,     G_COMMIT,
    ],
    # RGB CTL
    [
        xxxxxxx,    xxxxxxx,            xxxxxxx,                xxxxxxx,
        xxxxxxx,    KC.RGB_MODE_SWIRL,  KC.RGB_MODE_KNIGHT,     KC.RGB_MODE_BREATHE_RAINBOW,
        xxxxxxx,    KC.RGB_MODE_PLAIN,  KC.RGB_MODE_BREATHE,    KC.RGB_MODE_RAINBOW,
    ],
    # MIDI
    [
        KC.MIDI(30),    KC.MIDI(69),      KC.MIDI(70),       MIDI_OUT,
        KC.MIDI(67),    KC.MIDI(66),      KC.MIDI(65),       KC.MIDI(64),
        KC.MIDI(60),    KC.MIDI(61),      KC.MIDI(62),       KC.MIDI(63),
    ]
]

encoders.map = [    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.RGB_TOG)),   # MACROS
                    ((KC.RGB_AND, KC.RGB_ANI, xxxxxxx),     (KC.RGB_HUD,    KC.RGB_HUI,     _______   )),   # RGB CTL
                    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.RGB_TOG)),   # MIDI
                ]


# Point d'entrée principal du script. L'exécution du programme commence ici.
if __name__ == '__main__':
    keyboard.go()
