import shutil
import glob

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
number = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
year = ['2019','2020','2021','2022','2023']
specialty_origin = 'TF'
specialty_destiny = 'HC_Terapia_Física'


for j in range(len(year)):

    for i in range(len(months)):
        # Origin Path folder
        origin_path = f'C:/Users/juan.tamara/Desktop/HC_manager/files/stage/{specialty_origin}/'

        # Pattern to search for files starting with "2020-03-"
        files_pattern = f'{year[j]}-{number[i]}-*'

        # To Define the new destination path where you want to move the files
        destiny_path = f'C:/Users/juan.tamara/Desktop/HC_manager/{year[j]}/{number[i]}_{months[i]}/{specialty_destiny}/'
        #test_destiny_path = f'C:/Users/juan.tamara/Desktop/HC_manager/files/stage/{year[j]}/test/{number[i]}_{months[i]}/'

        # Use glob to get a list of files that match the pattern
        matching_files = glob.glob(origin_path + files_pattern)

        # Move each file to the destination folder
        for file in matching_files:
            shutil.move(file, destiny_path)

