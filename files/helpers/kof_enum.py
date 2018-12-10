from enum import Enum
from serpent.input_controller import KeyboardKey
class KOFKeyboardEnum(Enum):
    #方向按钮
    UP=KeyboardKey.KEY_UP
    DOWN=KeyboardKey.KEY_DOWN
    RIGHT=KeyboardKey.KEY_RIGHT
    LEFT=KeyboardKey.KEY_LEFT
    #操作按钮
    OP_1=KeyboardKey.KEY_NUMPAD_5
    OP_2=KeyboardKey.KEY_NUMPAD_1
    OP_3=KeyboardKey.KEY_NUMPAD_2
    OP_4=KeyboardKey.KEY_NUMPAD_3
