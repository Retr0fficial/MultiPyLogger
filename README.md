# MultiPyLogger

This Python script logs mouse position, active window title, and keyboard events, saving the logs into three separate text files (MouseLog.txt, WindowLog.txt, KeyboardLog.txt). The script uses the following libraries: time, threading, keyboard, pygetwindow, and pyautogui.
Dependencies

To install the required dependencies, run the following command:

bash

pip install keyboard pygetwindow pyautogui

Usage

    Ensure you have Python 3.x installed.
    Clone this repository or download the logger.py script.
    Open a terminal/command prompt and navigate to the folder containing the script.
    Run the script with the following command:

bash

python logger.py

The script will start monitoring and logging mouse positions, active window titles, and keyboard events. To stop the script, press the "esc" key.
Output

The script will generate three log files in the same directory as the script:

    MouseLog.txt: Contains the mouse positions (X and Y coordinates) and timestamps of when the positions were logged.
    WindowLog.txt: Contains the active window titles and timestamps of when the window titles were logged.
    KeyboardLog.txt: Contains the keyboard events (key names) and timestamps of when the keys were pressed.

Functions

    log_mouse_position(): Logs the mouse position (X and Y coordinates) continuously.
    log_active_window(): Logs the active window title continuously.
    log_key_pressed(e): Logs the key pressed event.

Note

Please be aware that using this script might raise privacy concerns, as it logs sensitive user input data. Make sure to use this script responsibly and inform others if you're using it on a shared computer.
