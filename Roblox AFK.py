import pygetwindow as gw
import pydirectinput
import pyautogui
import time
import ctypes

# Function to get the currently active window
def get_active_window():
    GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow
    return gw.getWindowsWithHandle(GetForegroundWindow())[0]

# Press space once at the start
try:
    roblox = gw.getWindowsWithTitle('Roblox')[0]  # Get the Roblox window
    roblox.activate()  # Bring the Roblox window to the front
except IndexError:
    print("Roblox window not found")
pydirectinput.press('space')  # Simulate pressing the spacebar

while True:
    time.sleep(14 * 60)  # Wait for 14 minutes
    try:
        roblox = gw.getWindowsWithTitle('Roblox')[0]  # Get the Roblox window
        current_window = get_active_window()  # Save the currently active window
        roblox.activate()  # Bring the Roblox window to the front
    except IndexError:
        print("Roblox window not found")
        continue

    # Save the current mouse position
    original_position = pyautogui.position()

    # Move the mouse to the middle of the Roblox window
    roblox_center = (roblox.left + roblox.width / 2, roblox.top + roblox.height / 2)
    pyautogui.moveTo(roblox_center)

    pydirectinput.press('space')  # Simulate pressing the spacebar

    # Move the mouse back to its original position
    pyautogui.moveTo(original_position)

    # Switch back to the previously active window
    current_window.activate()
