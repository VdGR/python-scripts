import pyautogui
import time


pos_select_at = 470, 550
pos_move_to = 174, 554

repetions = 4
x = 0

while x < repetions:
    print(f'Rep {x+1} of {repetions}')
    pyautogui.click(pos_select_at)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.dragTo(pos_move_to, duration=0.75, tween=pyautogui.easeInOutQuad)
    time.sleep(2)
    x += 1

