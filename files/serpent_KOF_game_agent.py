from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey
from .helpers.kof_enum import KOFKeyboardEnum
# from serpent.machine_learning.reinforcement_learning.ddqn import DDQN
import random
from serpent.window_controller import WindowController


class SerpentKOFGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

    def setup_play(self):
        print("进入setup_play")
        #所有的按键
        self.input_mapping={
			"W": [KOFKeyboardEnum.UP.value],
			"A": [KOFKeyboardEnum.LEFT.value],
			"S": [KOFKeyboardEnum.DOWN.value],
			"D": [KOFKeyboardEnum.RIGHT.value],
			"WA": [KOFKeyboardEnum.UP.value,KOFKeyboardEnum.LEFT.value],
			"WD": [KOFKeyboardEnum.UP.value,KOFKeyboardEnum.RIGHT.value],
			"SA": [KOFKeyboardEnum.DOWN.value,KOFKeyboardEnum.LEFT.value],
			"SD": [KOFKeyboardEnum.DOWN.value,KOFKeyboardEnum.RIGHT.value],
            "OP_1": [KOFKeyboardEnum.OP_1.value],
			"OP_2": [KOFKeyboardEnum.OP_2.value],
			"OP_3": [KOFKeyboardEnum.OP_3.value],
			"OP_4": [KOFKeyboardEnum.OP_4.value],
			"NONE": []
        }
    

    def handle_play(self, game_frame):
        input_key=random.choice(list(self.input_mapping))
        print("进入KOF97 输入:"+input_key)
        if input_key!='NONE':
            # key=self.input_mapping[input_key]
            # print(type(key))
            self.input_controller.tap_keys(self.input_mapping[input_key])
