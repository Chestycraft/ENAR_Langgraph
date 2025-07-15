import pyautogui
from schemas import State

def get_screensize(state:State):
    width, height = pyautogui.size()
    print(f"Screen size: {width}x{height}")