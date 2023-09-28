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

# Dicionário de valores para as teclas F2 a F5
valores_teclas = {
    'F2': "Fica R$ 129 com frete grátis e pagamento na entrega. 1 metro.",
    'F3': "As 2 saem por R$ 149 com frete grátis e pagamento na entrega. Todas com 1 metro.",
    'F4': "As 3 saem por R$ 199 com frete grátis e pagamento na entrega. Todas com 1 metro.",
    'F5': "As 4 saem por R$ 239 com frete grátis e pagamento na entrega. Todas com 1 metro.",
}

# Mensagem para a tecla F6
mensagem_f6 = "Amora\nAcerola\nAbacate\nBanana\nCajá\nCaju\nCarambola\nFigo\nFramboesa\nJaca\nJabuticaba\nLaranja\nLimão\nTangerinas\nPera\nPêssego\nUva\nNectarina\nEntre outras. Normalmente entre R$ 60 e 90. Em quais tem interesse?"

# Mensagem para a tecla F7
mensagem_f7 = "Olá, temos"
outra_mensagem_f7 = "Tem interesse em mais alguma frutífera?"

def disparar_mensagens(mensagem):
    # Copia a mensagem para a área de transferência (com acentos)
    pyperclip.copy(mensagem)

    # Obtém a posição atual do cursor
    x, y = pyautogui.position()

    # Clica no local atual do cursor
    pyautogui.click(x, y)

    # Cole o texto da área de transferência
    keyboard.press_and_release('ctrl+v')

    # Pequeno atraso
    time.sleep(0.5)

    # Pressiona Enter
    keyboard.press_and_release('enter')

    # Aguarda 1 segundo antes de inserir a próxima mensagem
    time.sleep(2)

# Associe a função disparar_mensagens à tecla F1 para enviar as duas mensagens em sequência
keyboard.add_hotkey('F1', lambda: [disparar_mensagens(mensagem) for mensagem in mensagens])

# Associe a função disparar_mensagens às teclas F2, F3, F4 e F5 para enviar as mensagens e valores correspondentes
for tecla, mensagem in valores_teclas.items():
    keyboard.add_hotkey(tecla, lambda mensagem=mensagem: disparar_mensagens(mensagem))

# Associe a função disparar_mensagens à tecla F6 para enviar a mensagem correspondente
keyboard.add_hotkey('F6', lambda: disparar_mensagens(mensagem_f6))

# Associe a função disparar_mensagens à tecla F7 para enviar as mensagens correspondentes
keyboard.add_hotkey('F7', lambda: [disparar_mensagens(mensagem_f7), disparar_mensagens(outra_mensagem_f7)])

while True:
    pass
