#SCRIPT PARA DESCARGAR IMÁGENES
Mediante este script se pueden descargar un conjunto de imágenes direcamente de _Google_.

##Índice
- [Prerequisitos](#prerequisitos)
- [Uso](#uso)
- [Output](#output)

##Prerequisitos
Antes de empezar con la ejecución de este programa hay que tener instalado un interprete de Python (algo obvio). Una vez hecho esto hay que ejecutar el siguiente comando para instalar una versión concreta de la librería que se va a usar:
```bash
pip install git+https://github.com/Joeclinton1/google-images-download.git
```
**SI INSTALAS OTRA VERSIÓN NO VA A FUNCIONAR**

##Uso
Para su uso lo primero es rellenar el fichero _nombres.txt_ con los nombres de las fotos que se quieren descargar (nombre por linea). \
Una vez rellenado hay que situarse en la carpeta raiz de este proyecto y ejecutar el siguiente comando:
```bash
python main.py
```
##Output
Al ejecutar este programa se va a crear una carpeta llamada _downloads_ la cual está compuesta por carpetas, cada una con el nombre de lo que se ha descargado y dentro de ella la imágen.

- ![JonAnderGithub](https://img.shields.io/github/followers/JonAnderAsua?style=social)
- ![jonan_bateria](https://img.shields.io/twitter/follow/jonan_bateria?style=social)

