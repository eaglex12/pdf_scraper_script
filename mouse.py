import pyautogui
import time

try:
    while True:
        # Perform a left-click at the current mouse position
        pyautogui.click()

        # Wait for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    print("Script stopped.")
