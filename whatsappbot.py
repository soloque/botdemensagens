import pyautogui
import time
import keyboard
import pyperclip

# Tempo de espera para você posicionar o cursor
print("Posicione o cursor em um campo de texto...")
time.sleep(5)

# Define uma lista de mensagens a serem inseridas
mensagens = [
    "Está sim",
    "Em quais frutíferas você tem interesse?"
]

def disparar_mensagens():
    for mensagem in mensagens:
        # Copia a mensagem para a área de transferência (com acentos)
        pyperclip.copy(mensagem)

        # Obtém a posição atual do cursor
        x, y = pyautogui.position()

        # Clica no local atual do cursor
        pyautogui.click(x, y)

        # Cole o texto da área de transferência
        keyboard.press_and_release('ctrl+v')

        # Pressiona Enter
        keyboard.press_and_release('enter')

        # Aguarda 1 segundo antes de inserir a próxima mensagem
        time.sleep(2)

# Associe a função disparar_mensagens à tecla F1
keyboard.add_hotkey('F1', disparar_mensagens)

while True:
    pass
