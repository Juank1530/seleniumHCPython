import shutil
import glob

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
number = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
year = '2023'
specialty = 'Notas_de_enfermería_yo_Evoluciones_de_las_notas'



for i in range(len(months)):
    # Ruta del directorio de origen
    ruta_directorio_origen = 'C:/Users/juan.tamara/Desktop/HC_manager/files/stage/nurseNotes/'

    # Patrón para buscar archivos que comienzan con "2020-03-"
    patron_archivos = f'{year}-{number[i]}-*'

    # Definir la nueva ruta de destino donde deseas mover los archivos
    ruta_carpeta_destino = f'C:/Users/juan.tamara/Desktop/HC_manager/{year}/{number[i]}_{months[i]}/{specialty}/'
    #ruta_carpeta_destino = f'C:/Users/juan.tamara/Desktop/HC_manager/files/stage/test_{number[i]}_{months[i]}/'

    # Usar glob para obtener una lista de archivos que coincidan con el patrón
    archivos_coincidentes = glob.glob(ruta_directorio_origen + patron_archivos)

    # Mover cada archivo a la carpeta de destino
    for archivo in archivos_coincidentes:
        shutil.move(archivo, ruta_carpeta_destino)

