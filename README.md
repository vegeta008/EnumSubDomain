# EnumDomain: Subdomain Scanner Tool

EnumDomain es una herramienta de escaneo de subdominios que permite realizar descubrimiento y análisis de subdominios de forma eficiente. Utilizando concurrencia y comprobaciones detalladas, esta herramienta es ideal para profesionales de la seguridad y entusiastas de la ciberseguridad que buscan identificar subdominios asociados a un dominio objetivo.

## **CARACTERÍSTICAS**

- **Resolución DNS:** Verifica y resuelve subdominios a direcciones IP.
- **Estado HTTP:** Comprueba el estado de respuesta HTTP de cada subdominio.
- **Cargador de diccionarios:** Permite cargar un archivo de texto con una lista personalizada de subdominios.
- **Configuración Personalizable:** Define configuraciones como el tiempo de espera (timeout), número de hilos (threads) y agentes de usuario (user agents).
- **Ejecución Concurrente:** Escaneo rápido y eficiente gracias al uso de `concurrent.futures`.
- **Interfaz CLI:** Totalmente configurable desde la línea de comandos con múltiples argumentos.

## **REQUISITOS**

- Python 3.6 o superior.


## **INSTALACIÓN**

1. Clona este repositorio:
   
   ```bash
   git clone https://github.com/tu_usuario/enumdomain.git
   cd enumdomain
   ```

## **USO**

Ejecuta el script desde la línea de comandos con los parámetros adecuados:

```bash
python3 enumdomain.py -d dominio.com -w wordlist.txt -t 10 -o resultados.json
```

### **ARGUMENTOS**

- `-d` o `--domain`: Dominio objetivo para el escaneo.
- `-w` o `--wordlist`: Ruta al archivo de diccionario que contiene subdominios.
- `-t` o `--threads`: Número de hilos para escaneo concurrente (por defecto, 5).
- `-o` o `--output`: Archivo de salida donde se guardarán los resultados en formato JSON.
- `--timeout`: Tiempo de espera para cada solicitud (por defecto, 10 segundos).

### **EJEMPLO DE EJECUCIÓN**

```bash
python3 enumdomain.py -d example.com -w subdomains.txt -t 10 -o output.json
```

Este comando escanea el dominio `example.com` utilizando una lista de subdominios (`subdomains.txt`), 10 hilos y guarda los resultados en `output.json`.

## **CONFIGURACIÓN DEL DICCIONARIO**

Asegúrate de proporcionar un archivo de texto con subdominios separados por líneas. Ejemplo:

```
www
mail
ftp
admin
```

Guarda este archivo como `subdomains.txt` y pásalo al script con el argumento `-w` o `--wordlist`.

## **RESULTADOS**

Los resultados del escaneo incluyen:
- Subdominios identificados.
- Dirección IP asociada.
- Estado HTTP de cada subdominio.

El formato de salida será un archivo JSON estructurado para facilitar el análisis.
