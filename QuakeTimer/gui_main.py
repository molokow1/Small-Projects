from console_type import quake_timer, item
import pyglet
import math
from pyglet.window import key


class GameLabel(pyglet.text.Label):
    """docstring for gameLabel"""
    def __init__(self, str, x, y, font_size=30):
        super(GameLabel, self).__init__()
        self.text = str
        self.font_name = 'Menlo'
        self.x = x
        self.y = y
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.font_size = font_size


class MainApp(object):
    """docstring for main_app"""

    def __init__(self):
        self.window = pyglet.window.Window()
        self.item_timer = quake_timer()
        self.input_str = ""
        self.current_item = self.item_timer.get_new_item()
        self.window.set_mouse_visible(True)
        self.waitForInput = True
        self.name_label = GameLabel(str(self.current_item.type),x=self.window.width//2, y=60)

        self.time_label = GameLabel('Time: ' + str(self.current_item.time),
                                            x=self.window.width // 2, y=100)
        self.ans_label = pyglet.text.Label(str(self.current_item.answer), font_name='Menlo',
                                           font_size=30,
                                           x=self.window.width // 2, y=140,
                                           anchor_x='center', anchor_y='center')
        self.input_label = pyglet.text.Label("Input Here", font_name='Menlo',
                                             font_size=30,
                                             x=self.window.width // 2, y=180,
                                             anchor_x='center', anchor_y='center')
        self.status_label = pyglet.text.Label("Status Here", font_name='Menlo',
                                             font_size=30,
                                             x=self.window.width // 2, y=220,
                                             anchor_x='center', anchor_y='center')
        self.title_label = pyglet.text.Label("Quake Timer", font_name='Menlo',
                                              font_size=48,
                                              x=self.window.width // 2, y=380,
                                              anchor_x='center', anchor_y='center')

    def run(self):

        @self.window.event
        def on_draw():
            self.window.clear()
            self.time_label.draw()
            self.name_label.draw()
            # self.ans_label.draw()
            self.input_label.draw()
            self.status_label.draw()
            self.title_label.draw()

        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == key.A:
                self.ans_label.text = 'A pressed'
            elif symbol == key.B:
                self.ans_label.text = 'B pressed'
            elif symbol == key.ENTER:
                check_answer()

        @self.window.event
        def on_text(text):
            if text.isdigit():
                parse_ans_input(text)

        def parse_ans_input(usr_input):
            if self.waitForInput:
                if len(self.input_label.text) >= 2:
                    self.input_label.text = usr_input
                else:
                    self.input_label.text += usr_input

        def check_answer():
            self.status_label.text = "Item updated"
            current_respond = self.input_label.text
            self.waitForInput = True
            if current_respond == str(self.current_item.answer):
                self.status_label.text = "Correct!"
            else:
                self.status_label.text = "Try again"

            update_item()

        def update_item():
            self.current_item = self.item_timer.get_new_item()
            self.name_label.text = self.current_item.type
            self.time_label.text = "Time: " + str(self.current_item.time)
            self.ans_label.text = "Ans: " + str(self.current_item.answer)



        pyglet.app.run()


if __name__ == '__main__':
    test = MainApp()
    test.run()
