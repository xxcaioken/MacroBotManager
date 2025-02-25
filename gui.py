import tkinter as tk
import threading
import keyboard_listener
import shortcut_manager

def center_window(window, width, height):
    """Função para centralizar a janela."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')

def start_script():
    """Inicia a escuta do teclado em uma thread separada."""
    thread = threading.Thread(target=keyboard_listener.start_keyboard_listener, daemon=True)
    thread.start()

def stop_script():
    """Para o listener de teclado corretamente."""
    keyboard_listener.stop_keyboard_listener()

root = tk.Tk()
root.title("Controle do Bot")
root.geometry("300x200")

center_window(root, 300, 200)

tk.Label(root, text="Controle do Bot de Teclado").pack(pady=10)

tk.Button(root, text="Iniciar Bot", command=start_script).pack(pady=5)

tk.Button(root, text="Parar Bot", command=stop_script).pack(pady=5)

tk.Button(root, text="Gerenciar Atalhos", command=shortcut_manager.open_shortcut_manager).pack(pady=5)

tk.Button(root, text="Sair", command=root.quit).pack(pady=5)

root.mainloop()
