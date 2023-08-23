import shutil
from selenium import webdriver

# Supongamos que has descargado un archivo con Selenium y sabes su ruta actual
ruta_archivo_actual = "C:/Users/juan.tamara/Desktop/1/2/New Text Document.txt"

# Definir la nueva ruta de destino donde deseas mover el archivo
ruta_carpeta_destino = "C:/Users/juan.tamara/Desktop/1/"

shutil.move(ruta_archivo_actual, ruta_carpeta_destino)
