import pyautogui
import time

pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código estiver rodando")
pyautogui.PAUSE = 0.2

# Abrir o Google Drive no computador
pyautogui.press('winleft')
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/my-drive")
time.sleep(1)
pyautogui.press('enter')

# Entrar na Área de Trabalho
pyautogui.hotkey('winleft', 'd')

# Selecionar o arquivo de backup
# pyautogui.position() / Encontra a posição na tela
pyautogui.moveTo(114, 111)
pyautogui.mouseDown()
time.sleep(1)
pyautogui.moveTo(912, 589)

# Anexando o arquivo no Google Drive
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()

# Esperar 5 segundos
time.sleep(5)

pyautogui.alert("O código acabou de rodar. Pode usar o seu computador novamente")