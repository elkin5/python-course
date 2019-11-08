# Preparando nuestro ambiente
Para comenzar, será necesario que instalemos python y aprovechando la ocasión, utilizaremos la última versión disponible a la fecha.

## Instalar Python 3.8 ##

1. Instalar librerías necesarias
``` bash
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
```

2. Descargar y extraer Python
``` bash
cd /opt
sudo wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
sudo tar xzf Python-3.8.0.tgz
```

3. Compilar
``` bash
cd Python-3.8.0
sudo ./configure --enable-optimizations
sudo make altinstall
```

4. Chequear versión
``` bash
python3.8 -V
```

5. Borrar archivos temporales
``` bash
cd /opt
sudo rm -f Python-3.8.0.tgz
```

## Instalación de Virtualenv
Si no sabes qué es virtualenv, puedes aprender un poco más sobre su uso, ventajas, etc en el siguiente enlace: ...

1. Instalar virtualenv
``` bash
sudo apt-get install python3-virtualenv
```

2. Crear un ambiente
``` bash
# Reemplazar el path por su directorio
cd /media/DATOS/LUCAS/Programming/Python/azul_web
sudo virtualenv -p python3.8 ambiente
```

3. Activar el ambiente
``` bash
source /media/DATOS/LUCAS/Programming/Python/azul_web/ambiente/bin/activate

# (ambiente) usr@...
```	

4. Chequear la versión de Python y actualizar pip
``` bash
python -V

# Python 3.8.0

python -m pip install --upgrade pip
```	
Ya tenemos python y pip instalados en nuestro ambiente virtual!
 
## Intérprete

Solo nos resta verificar que Python funcione correctamente. Para ello, utilizaremos el intérprete para imprimir un "Hola mundo".
1. Abrir el intérprete
```bash
python

# Python 3.8.0 (default, ...
```

2. Imprimir un Hola mundo con el siguiente statement:
``` python
print ("Hola mundo!")
``` 
Pero... qué es un statement? Un statement es cualquier instrucción que pueda ser ejecutada por el intérprete de Python.
Al ejecutar la instrucción anterior, verás en pantalla el mensaje "Hola mundo!", esto quiere decir que todo funciona!

3. Salir del intérprete
Para salir del intérprete de Python, utiliza la instrucción:
``` python
quit()
```

## Volver a la consola

Para cerrar nuestro ambiente virutal, solo ingresa el siguiente comando:
``` bash
deactivate
```
