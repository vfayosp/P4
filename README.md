PAV - P4: reconocimiento y verificación del locutor
===================================================

Obtenga su copia del repositorio de la práctica accediendo a [Práctica 4](https://github.com/albino-pav/P4)
y pulsando sobre el botón `Fork` situado en la esquina superior derecha. A continuación, siga las
instrucciones de la [Práctica 2](https://github.com/albino-pav/P2) para crear una rama con el apellido de
los integrantes del grupo de prácticas, dar de alta al resto de integrantes como colaboradores del proyecto
y crear la copias locales del repositorio.

También debe descomprimir, en el directorio `PAV/P4`, el fichero [db_8mu.tgz](https://atenea.upc.edu/pluginfile.php/3145524/mod_assign/introattachment/0/spk_8mu.tgz?forcedownload=1)
con la base de datos oral que se utilizará en la parte experimental de la práctica.

Como entrega deberá realizar un *pull request* con el contenido de su copia del repositorio. Recuerde
que los ficheros entregados deberán estar en condiciones de ser ejecutados con sólo ejecutar:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.sh
  make release
  run_spkid mfcc train test classerr verify verifyerr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Recuerde que, además de los trabajos indicados en esta parte básica, también deberá realizar un proyecto
de ampliación, del cual deberá subir una memoria explicativa a Atenea y los ficheros correspondientes al
repositorio de la práctica.

A modo de memoria de la parte básica, complete, en este mismo documento y usando el formato *markdown*, los
ejercicios indicados.

## Ejercicios.

### SPTK, Sox y los scripts de extracción de características.

- Analice el script `wav2lp.sh` y explique la misión de los distintos comandos, y sus opciones, involucrados
  en el *pipeline* principal (`sox`, `$X2X`, `$FRAME`, `$WINDOW` y `$LPC`).

  `sox`-> Se utiliza para convertir de formato wav a formato raw y con una frecuencia de 16k para despues
  poderlo gestionar con el SPTK.
  `$X2X`-> Se utiliza para convertir de un tipo de dato a otro. En nuestro caso de short a float.
  `$FRAME`-> Se utiliza para dividir la señal en tramas. En nuestro caso de 240 muestras con 80 muestras de salto.
  `$WINDOW`-> Se utiliza para enventanar cada uno de estas tramas. Se puede escoger el filtro y cuantas 
              muestras se quieren enventanar.
  `$LPC`-> Se utiliza para calcular los coeficientes de predicción lineal de las tramas. Se puede escoger el orden
          del predictor y con cuantas muestras se quiere hacer.

- Explique el procedimiento seguido para obtener un fichero de formato *fmatrix* a partir de los ficheros
  de salida de SPTK (líneas 41 a 47 del script `wav2lp.sh`).

  Primero se utilizan los comandos anteriores en cascada para sacar los predictores de cada una de las tramas,
  seguidamente se crea la cabecera de este tipo de archivos especificando el numero de columnas y el numero de filas.

  * ¿Por qué es conveniente usar este formato (u otro parecido)?
  
  Para asi tener mejor estructurados los datos y poder sacar la información de manera sencilla

- Escriba el *pipeline* principal usado para calcular los coeficientes cepstrales de predicción lineal
  (LPCC) en su fichero <code>scripts/wav2lpcc.sh</code>:

  sox $inputfile -t raw -e signed -b 16 - | $X2X +sf | $FRAME -l 240 -p 80 | $WINDOW -l 240 -L 240 |
	$LPC -l 240 -m $lpcc_order | $LPC2C -m $lpcc_order -M $lpcc_order > $base.lpcc

- Escriba el *pipeline* principal usado para calcular los coeficientes cepstrales en escala Mel (MFCC) en
  su fichero <code>scripts/wav2mfcc.sh</code>:

  sox $inputfile -t raw -e signed -b 16 - | $X2X +sf | $FRAME -l 240 -p 80 |  $MFCC -s 8 -l 240 -L 512 -m $mfcc_order > $base.mfcc

### Extracción de características.

- Inserte una imagen mostrando la dependencia entre los coeficientes 2 y 3 de las tres parametrizaciones
  para una señal de prueba.

  ![Comparación](https://github.com/vfayosp/P4/blob/fayos-valverde/fotos%20y%20graficos/comparacion_lp_lpcc_mfcc.png)
  
  + ¿Cuál de ellas le parece que contiene más información?
  
  Parece tener más información los componenetes lpcc, ya que estan más concentrados en dos puntos. Los otros coeficientes están
  más esparcidos.

- Usando el programa <code>pearson</code>, obtenga los coeficientes de correlación normalizada entre los
  parámetros 2 y 3, y rellene la tabla siguiente con los valores obtenidos.

  |                        | LP   | LPCC | MFCC |
  |------------------------|:----:|:----:|:----:|
  | &rho;<sub>x</sub>[2,3] |      |      |      |
  
  + Compare los resultados de <code>pearson</code> con los obtenidos gráficamente.
  
- Según la teoría, ¿qué parámetros considera adecuados para el cálculo de los coeficientes LPCC y MFCC?

  LPCC: Orden lpcc 19
        Orden cepstrum 26
  MFCC: Orden mfcc 13
        Orden mel-cepstrum 19

### Entrenamiento y visualización de los GMM.

Complete el código necesario para entrenar modelos GMM.

- Inserte una gráfica que muestre la función de densidad de probabilidad modelada por el GMM de un locutor
  para sus dos primeros coeficientes de MFCC.

  ![GMM LOC04](https://github.com/vfayosp/P4/blob/fayos-valverde/fotos%20y%20graficos/gmm_ses004.png)
  
- Inserte una gráfica que permita comparar los modelos y poblaciones de dos locutores distintos (la gŕafica
  de la página 20 del enunciado puede servirle de referencia del resultado deseado). Analice la capacidad
  del modelado GMM para diferenciar las señales de uno y otro.

  Modelos GMM del locutor 4 y 44:
  Datos de entrenamiento del locutor 4
  ![GMM 4 y 44 LOC04](https://github.com/vfayosp/P4/blob/fayos-valverde/fotos%20y%20graficos/gmm_ses04_lpcc_ses04.png)

  Datos de entrenamiento del locutor 44
  ![GMM 4 y 44 LOC44](https://github.com/vfayosp/P4/blob/fayos-valverde/fotos%20y%20graficos/gmm_ses44_lpcc_ses44.png)

### Reconocimiento del locutor.

Complete el código necesario para realizar reconociminto del locutor y optimice sus parámetros.

- Inserte una tabla con la tasa de error obtenida en el reconocimiento de los locutores de la base de datos
  SPEECON usando su mejor sistema de reconocimiento para los parámetros LP, LPCC y MFCC.

  |                        | LP   | LPCC | MFCC |
  |------------------------|:----:|:----:|:----:|
  | Tasa de error          |9,04% |0,76% |8,79% |

### Verificación del locutor.

Complete el código necesario para realizar verificación del locutor y optimice sus parámetros.

- Inserte una tabla con el *score* obtenido con su mejor sistema de verificación del locutor en la tarea
  de verificación de SPEECON. La tabla debe incluir el umbral óptimo, el número de falsas alarmas y de
  pérdidas, y el score obtenido usando la parametrización que mejor resultado le hubiera dado en la tarea
  de reconocimiento.

  |                        |         LP       |       LPCC       |       MFCC       |
  |------------------------|:----------------:|:----------------:|:----------------:|
  | Cost                   |       83,4       |       13,2       |       76,4       |
  | Threshold              |0.924207239399991 |0.893346727121306 |0.9092007283127   |
  | Missed                 |      159/255     |      26/255      |      191/255     |
  | False Alarm            |      2/1000      |      0/1000      |      0/1000      |
 
### Test final y trabajo de ampliación.

- Recuerde adjuntar los ficheros `class_test.log` y `verif_test.log` correspondientes a la evaluación
  *ciega* final.

- Recuerde, también, enviar a Atenea un fichero en formato zip o tgz con la memoria con el trabajo
  realizado como ampliación, así como los ficheros `class_ampl.log` y/o `verif_ampl.log`, obtenidos como
  resultado del mismo.
