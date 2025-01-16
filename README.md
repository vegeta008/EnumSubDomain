#EnumDomain: Subdomain Scanner Tool

EnumDomain es una herramienta de escaneo de subdominios que permite realizar descubrimiento y análisis de subdominios de forma eficiente. Utilizando concurrencia y comprobaciones detalladas, esta herramienta es ideal para profesionales de la seguridad y entusiastas de la ciberseguridad que buscan identificar subdominios asociados a un dominio objetivo.

Características

Resolución DNS: Verifica y resuelve subdominios a direcciones IP.

Estado HTTP: Comprueba el estado de respuesta HTTP de cada subdominio.

Cargador de diccionarios: Permite cargar un archivo de texto con una lista personalizada de subdominios.

Configuración Personalizable: Define configuraciones como el tiempo de espera (timeout), número de hilos (threads) y agentes de usuario (user agents).

Ejecución Concurrente: Escaneo rápido y eficiente gracias al uso de concurrent.futures.

Interfaz CLI: Totalmente configurable desde la línea de comandos con múltiples argumentos.

Requisitos

Python 3.6 o superior.

Bibliotecas requeridas (instaladas automáticamente si usas el siguiente comando):

requests

socket

argparse

concurrent.futures

Instalación

Clona este repositorio:

git clone https://github.com/tu_usuario/enumdomain.git
cd enumdomain

(Opcional) Crea un entorno virtual:

python3 -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate

Instala las dependencias necesarias:

pip install -r requirements.txt

Uso

Ejecuta el script desde la línea de comandos con los parámetros adecuados:

python3 enumdomain.py -d dominio.com -w wordlist.txt -t 10 -o resultados.json

Argumentos

-d o --domain: Dominio objetivo para el escaneo.

-w o --wordlist: Ruta al archivo de diccionario que contiene subdominios.

-t o --threads: Número de hilos para escaneo concurrente (por defecto, 5).

-o o --output: Archivo de salida donde se guardarán los resultados en formato JSON.

--timeout: Tiempo de espera para cada solicitud (por defecto, 10 segundos).

Ejemplo de ejecución

python3 enumdomain.py -d example.com -w subdomains.txt -t 10 -o output.json

Este comando escanea el dominio example.com utilizando una lista de subdominios (subdomains.txt), 10 hilos y guarda los resultados en output.json.

Configuración del diccionario

Asegúrate de proporcionar un archivo de texto con subdominios separados por líneas. Ejemplo:

www
mail
ftp
admin

Guarda este archivo como subdomains.txt y pásalo al script con el argumento -w o --wordlist.

Resultados

Los resultados del escaneo incluyen:

Subdominios identificados.

Dirección IP asociada.

Estado HTTP de cada subdominio.

El formato de salida será un archivo JSON estructurado para facilitar el análisis.

Contribución

Si deseas contribuir a este proyecto:

Haz un fork del repositorio.

Crea una rama con tu característica o corrección.

git checkout -b mi-rama

Realiza un pull request y explícanos tu contribución.

Licencia

Este proyecto está licenciado bajo la Licencia MIT.

Contacto

Para dudas o sugerencias, puedes contactar al desarrollador en:

GitHub: tu_usuario

Email: tu_correo@ejemplo.com
