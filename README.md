# Analizador Lexico y Sintactico de Dart

## Descripcion
El objetivo de este proyecto es crear un analizador lexico y sintactico que cumpla las caracteristicas del lenguaje de programacion Dart, en donde se pase como input un archivo de texto con un codigo fuente en Dart, y el lexer lo que realizara es un analisis linea por linea de cada uno de los tokens detectados.

## Ejemplo de ejecucion - Analizador Lexico

Al ejecutar el codigo, se va a leer el archivo `input.txt`, en este archivo se encuentra todo el codigo fuente que va a ser evaluado por el lexer.

Se va a mostrar un ouput, en el cual se va a leer cada linea del input.txt y se va a hacer la respectiva evaluacion de cada token, esto se va a mostrar en consola de la siguiente forma:

```
LexToken(PRINT,'print',80,2)
LexToken(LPARENT,'(',80,7)
LexToken(COMILLAS_DOBL,'"',80,8)
LexToken(VARIABLE,'Precio',80,9)

```
Donde LexToken() es el token detectado, el primer argumento es el nombre del token, el segundo argumento es la palabra detectada que hizo match con la expresion regular correpondiente, el tecer argumento es la linea en la que se encontro el token, y el cuarto es la ubicacion de la linea en la que se encontro.

## Ejemplo de ejecucion - Analizador Sintactico
