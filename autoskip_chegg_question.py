import time
import threading
from pynput.mouse import Button, Controller, Listener

left_button = Button.left
start_stop_button = Button.right
exit_button = Button.middle

skip_button = (350, 950)
reason_button = (430, 750)
submit_button = (1400, 880)

class ClickMouse(threading.Thread):
    def __init__(self, button):
        super(ClickMouse, self).__init__()
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        print("Running", flush=True)
        self.running = True

    def stop_clicking(self):
        print("Paused", flush=True)
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.position = skip_button
                mouse.click(left_button)

                time.sleep(1)
                mouse.position = reason_button
                mouse.click(left_button)

                time.sleep(0.4)
                mouse.position = submit_button
                mouse.click(left_button)
                print("skipped", flush=True)

                time.sleep(10)
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(left_button)
time.sleep(8)
click_thread.start()


def on_click(x, y, button, pressed):
    if pressed:
        if button == start_stop_button:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif button == exit_button:
            click_thread.exit()
            listener.stop()


with Listener(on_click=on_click) as listener:
    listener.join()
