import pyautogui

# Espera unos segundos para que puedas posicionar el cursor en la posición deseada
print("Posiciona el cursor en la ubicación deseada en 5 segundos...")
pyautogui.PAUSE = 5

# Obtiene y muestra las coordenadas del cursor
current_mouse_x, current_mouse_y = pyautogui.position()
print(f"Coordenadas del cursor: X={current_mouse_x}, Y={current_mouse_y}")
