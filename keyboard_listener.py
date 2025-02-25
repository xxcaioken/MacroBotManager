import time
import keyboard
import threading

running = False 
listener_thread = None
shortcuts = {}

def on_key_event(event):
    """Função chamada quando uma tecla é pressionada."""
    if event.name in shortcuts:
        keyboard.press_and_release('backspace')
        text = shortcuts[event.name]
        if "\n" in text:
            escrever_mensagem(text)
        else:
            keyboard.write(shortcuts[event.name])

def escrever_mensagem(text):
    """Função para digitar a mensagem automaticamente."""
    for linha in text.split("\n"):
        keyboard.write(linha)
        keyboard.press_and_release("shift+enter")
        time.sleep(0.1)

def load_shortcuts():
    """Carrega os atalhos do banco de dados."""
    global shortcuts
    import database
    shortcuts = {key: text for key, text in database.get_shortcuts()}

def start_keyboard_listener():
    """Inicia o listener de teclado em uma thread."""
    global running, listener_thread
    if running:
        return

    running = True
    load_shortcuts()
    listener_thread = threading.Thread(target=run_keyboard_listener, daemon=True)
    listener_thread.start()

def run_keyboard_listener():
    """Função que mantém o listener ativo."""
    keyboard.on_press(on_key_event)
    while running:
        keyboard.wait()

def stop_keyboard_listener():
    """Para o listener de teclado."""
    global running
    running = False
    keyboard.unhook_all()