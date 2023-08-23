import os
import re


# Función para reemplazar caracteres especiales, tildes y espacios en blanco por guiones bajos
def clean_folder_name(name):
    name = re.sub(r'[^\w\s-]', '', name)  # Remover caracteres especiales
    name = re.sub(r'\s', '_', name)  # Reemplazar espacios en blanco por guiones bajos
    return name


# Lista de nombres de carpetas
folder_names = [
    'Admisión PAD',
    'Escala Glaswo',
    'Escala Karnofsky',
    'Escala Barthel',
    'Medicina General',
    'Rehabilitación',
    'Psicología',
    'Clínica de heridas',
    'Epicrisis',
    'Evoluciones HC',
    'Notas de enfermería y/o Evoluciones de las notas',
    'Formulación',
    'Procedimientos',
    'Laboratorios',
    'Signos vitales',
    'FONO HC',
    'FONO Evolución',
    'Parálisis Facial',
    'Parálisis Facial Evolución',
    'HC Ocupacional',
    'Evoluciones Ocupacional',
    'Objetivos Ocupacional',
    'HC Terapia Física',
    'Terapia Física objetivos',
    'Terapia Física Movilidad MI',
    'Terapia Física Movilidad MS',
    'Terapia Física Evoluciones',
    'HC Terapia Física Pediátrica',
    'HC Terapia Física Pediátrica Evoluciones',
    'HC Terapia Respiratoria',
    'Terapia Respiratoria Evoluciones',
    'HC Psicología',
    'Psicología Evoluciones'
]

# Lista de nombres de meses en español
meses = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre',
    'Diciembre'
]

# Carpeta raíz
root_folder = "HC_manager"

# Crear carpetas por año y mes
for year in range(2019, 2024):
    year_folder = os.path.join(root_folder, str(year))
    os.makedirs(year_folder, exist_ok=True)
    for month in range(1, 13):
        month_name = meses[month - 1]
        month_folder = os.path.join(year_folder, str(month).zfill(2) + "_" + month_name)
        os.makedirs(month_folder, exist_ok=True)

        # Crear carpetas internas
        for folder_name in folder_names:
            folder_path = os.path.join(month_folder, clean_folder_name(folder_name))
            os.makedirs(folder_path, exist_ok=True)
