import pyautogui
import time

pyautogui.press('win')
time.sleep(2)
pyautogui.write('teleg')
time.sleep(2)
pyautogui.press('enter')
pyautogui.moveTo(50, 150)
time.sleep(1)
pyautogui.click()
pyautogui.moveTo(170, 200)
time.sleep(2)
pyautogui.click()
time.sleep(2)
pyautogui.write("ola, estou testando o de envio automatico de msg")
time.sleep(2)
pyautogui.press('enter')

