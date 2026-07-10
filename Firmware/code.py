import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler

from kmk.modules.display import Display
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),)
]

encoder_handler.pins = (
    (board.D9, board.D10, None),
)

display = Display()
display.driver = SSD1306(
    width=128,
    height=64,
    i2c=board.I2C(sda=board.D4, scl=board.D5)
)

keyboard.modules.append(display)

keyboard.matrix = KeysScanner(
    pins=[
        board.D0,
        board.D1,
        board.D2,
        board.D3,
        board.D6,
        board.D7,
        board.D8,
    ],
    value_when_pressed=False,
    pull=True
)

keyboard.keymap = [
    [
        KC.LALT(KC.A),
        KC.LALT(KC.V),
        KC.LALT(KC.Y),
        KC.LALT(KC.H),
        KC.LALT(KC.SHIFT(KC.S)),
        KC.NO,
        KC.NO,
    ]
]

if __name__ == "__main__":
    keyboard.go()