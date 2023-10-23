# incorporador-de-bloques

La función de este programa es escoger un fichero entre todos los de un directorio que cumpla lo siguiente respecto a otro fichero dado: los dos ficheros son completamente iguales a diferencia de que el del directorio tiene una línea adicional en la que aparecen un número hexadecimal de ocho dígitos, un número hexadecimal de dos dígitos y el número 100 separados por tabuladores. En el caso de [incorporador.py](incorporador.py), el fichero elegido será el primer fichero del directorio que más trabajo tenga atribuido al él. En el caso de [incorporador-ponderado.py](incorporador-ponderado.py), todos los ficheros válidos tendran una probabilidad de ser elegidos proporcional a la cantidad de ceros que tenga su hash.

**Pasos a seguir para usar el programa:**

1. Descarga el fichero llamado [incorporador.py](incorporador.py), ya sea manualmente desde el repositorio en github, ya sea clonando el repositorio en tu máquina local.
2. Asegurate de tener python instalado en tu máquina. Si no tienes python, puedes descargarlo desde [aquí](https://www.python.org/downloads/). Otra opción es ejecutar el código en [Google Colab](https://colab.google).
3. En la terminal, ejecuta el script (ej. *python incorporador.py*). Si se está usando Google Colab, simplemente haz click en el boton de ejecutar.
4. Escribe las direcciones en tu máquina del fichero y del directorio de ficheros. El fichero y el directorio deben estar dentro del mismo directorio.
5. El programa devolverá el nombre del fichero que ha escogido o el texto "No hay ficheros que cumplan las condiciones" en el caso de que no haya ficheros en el directorio que cumplan las condiciones.

Para probar el programa se puede usar el [fichero.txt](fichero.txt) como el fichero original y el directorio [ejemplos](ejemplos) como directorio con ficheros candidatos.
