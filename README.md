# Selenium HC Python

## Automatizaciones con Selenium y Phyton (Descargas de HC)

### Descripción
Estos scripts automatizados permiten acceder a cada uno de los apartados de la plataforma Manager y descargar la Historia Clínica de cada paciente, en el equipo local donde se ejecute.

### Requerimientos para ejecutar

Para poder ejecutar estos scripts, asegúrate de cumplir con los siguientes requerimientos:

1. **Python**: Debes tener instalado python en su versión 3 para su instalación se pude usar la documentación ofical de Python en la [página de Python](https://www.python.org/).
2. **Selenium**: Debes tener instalado el paquete de Selenium. Puedes instalarlo utilizando el siguiente comando: **pip install selenium**
3. Se recomienda utilizar la versión más reciente de Selenium para garantizar un funcionamiento óptimo.
4. **WebDriver del Navegador**: También necesitas el WebDriver del navegador que planeas utilizar con Selenium. Asegúrate de consultar la documentación oficial de Selenium para obtener información sobre cómo configurar y descargar el WebDriver adecuado para tu navegador.
5. **Archivo config.py**: Dentro de cada script se hace referencia al archivo config.py, este archivo contiene:
	1. La URL de la plataforma donde se descargan las HC.
	2. Usuario y contraseña, para hacer el login
	3. Listado de documentos de los pacientes 
	4. Listado de nombres con los que se van a guardar los archivos en el equipo local           

**Ejemplo**:

```
username = "user"  
password = "Password"  
url = "mysite.com"  
  
id_patient = [  
'id_paciente1',
id_paciente2',
etc...
]  
  
files_names = [  
'name1',
'name2',
etc...   
]
```

### Configuración

Antes de ejecutar los scripts, asegúrate de configurar adecuadamente el WebDriver y cualquier otra configuración necesaria según la documentación de Selenium en la [página de Selenium](https://www.selenium.dev/downloads/).

¡Listo! Con estos requisitos cumplidos, estarás listo para utilizar los scripts de automatización y descargar las Historias Clínicas de los pacientes desde la plataforma Manager.
