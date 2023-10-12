
# Déjame escuchar la música

# Introducción
# * [Etapa 1. Descripción de los datos]
#     * [Conclusiones]
# * [Etapa 2. Preprocesamiento de datos]
#     * [2.1 Estilo del encabezado]
#     * [2.2 Valores ausentes]
#     * [2.3 Duplicados]
#     * [2.4 Conclusiones]
# * [Etapa 3. Prueba de hipótesis]
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades]
#     * [3.2 Hipótesis 2: preferencias musicales los lunes y los viernes]
#     * [3.3 Hipótesis 3: preferencias de género en Springfield y Shelbyville]
# * [Conclusiones]

# En este proyecto, se comparará las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar las hipótesis a continuación y 
# comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Probar tres hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la cuidad.
# 2. Los lunes por la mañana, los habitantes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre con los viernes por la noche.
# 3. Los oyentes de Springfield y Shelbyville tienen preferencias distintas. En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap.
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `https://practicum-content.s3.us-west-1.amazonaws.com/datasets/music_project_en.csv`. 
# No hay ninguna información sobre la calidad de los datos, así que se necesitará examinarlos antes de probar las hipótesis.
# 
# Primero, se evaluarán la calidad de los datos y  se verá si los problemas son significativos. Entonces, durante el preprocesamiento de datos, se tomarán en cuenta los problemas más críticos.
# 
# El proyecto consistirá en tres etapas:
#  1. Descripción de los datos
#  2. Preprocesamiento de datos
#  3. Prueba de hipótesis
# 

# ## Etapa 1. Descripción de los datos 
# 
# Abrir los datos y examinarlos.

# importar pandas
import pandas as pd


# leer el archivo y almacenarlo en df
df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/music_project_en.csv')
df

# obtener las 10 primeras filas de la tabla df con el méetodo head()
df.head(10)

# obtener información general sobre los datos en df, con info() obtenemos dicha información
df.info()

# Estas son las observaciones sobre la tabla. Contiene siete columnas. Todas almacenan el mismo tipo de datos: `object` (objeto).
# 
# Según la documentación:
# - `'userID'` — identificador del usuario o la usuaria;
# - `'Track'` — título de la canción;
# - `'artist'` — nombre del artista;
# - `'genre'` — género musical;
# - `'City'` — ciudad del usuario o la usuaria;
# - `'time'` — hora exacta en la que se reprodujo la pista;
# - `'Day'` — día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas, otros, en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. Algunos encabezados no son tan claros o descriptivos respecto a los datos de la columna.
# 
# 
# `Observaciones:`
# 
# `1. ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?`
#        Todos los datos son de tipo objeto, que son para describir tipos de datos más general, como strings, listas, etc.
#        
# 
# `2. ¿Hay suficientes datos para proporcionar respuestas a nuestras tres hipótesis, o necesitamos más información?`
#       Sí, con los datos proporcionados se puede dar respuesta a las hipótesis planteadas, ya que el Dataset contiene
#       información de ambas ciudades sobre las preferencias músicales, aunque tiene valores ausentes.
# 
# `3. ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`
#        Hay valores ausentes en las columnas 'Track', 'artist' y 'genre', no se puede afirmar hasta este punto si hay valores
#        duplicados, se tiene que continuar con el precesamiento de datos para verificarlo. Los tipos de datos son correctos y se
#        puede trabajar con ellos sin necesidad de cambiarlos.


# ## Etapa 2. Preprocesamiento de datos 
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. 

# Corregir el formato en los encabezados de la tabla.

# la lista de encabezados para la tabla df, se usa el atributo columns para obtener una lista con los nombres de las columnas
col_names = df.columns
col_names

# Se cambian los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * todos los caracteres deben ser minúsculas;
# * se eliminan los espacios;
# * si el nombre tiene varias palabras, se utiliza snake_case.

# Se ponen todos los caracteres en minúsculas e imprime el encabezado de la tabla de nuevo:

# bucle en los encabezados poniendo todo en minúsculas
# se emplea un bucle for para iterar sobre la lista con los nombres de las columnas
lower_col_names = [] # se define una nueva lista vacia para guardar los nuevos nombre de las columnas en minúscula

for col in col_names:
    lower_names = col.lower()
    lower_col_names.append(lower_names)

print(lower_col_names)

# Ahora se eliminan los espacios al principio y al final de los encabezados:
# bucle en los encabezados eliminando los espacios
# un buble for para iterar sobre los la lista lower_col_names que tiene los nombre de la columna en minúscula

stripped_col_names = [] # se define una nueva lista vacia para guardar los nuevos nombre de las columnas en minúscula y sin espacios al inicio y al final
for col in lower_col_names:
    stipped_names = col.strip()
    stripped_col_names.append(stipped_names)

print(stripped_col_names)

# Se aplica snake_case al encabezado userID y se imprime el encabezado de la tabla:

# cambiar el nombre del encabezado "user_id"
# Se asignan los nuevos nombres de columna
df.columns = stripped_col_names

# Después se cambia el nombre del encabezado 'userid' a 'user_id' con el método rename
df = df.rename(columns= {'userid':'user_id'})


print(df.columns)

# comprobar el resultado: la lista de encabezados
df.columns

# ### Valores ausentes <a id='missing_values'></a>

# calcular el número de valores ausentes

# Emplear isna() y sum() para encontrar el número de valores ausentes
df.isna().sum()


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente se pueden reemplazar con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. 
# Pero no tenemos esa oportunidad en este proyecto. Así que se tendrán que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. 
# Para hacer esto, crea una lista `columns_to_replace`, recorre sobre ella con un bucle `for`, y para cada columna se reemplazan los valores ausentes en ella:

# Porcentaje de valores ausentes a reemplazar con 'unknown'

num_ausentes = df.isna().sum().sum() # Cálculo para sumar todos los valores ausentes
num_no_ausentes = df.notnull().sum().sum() # # Cálculo para sumar todos los valores no ausentes
total_datos = num_ausentes + num_no_ausentes # Suma para obtener el total de los datos

# Cálculo del porcentaje de valores ausentes, el resultado se redondea 1 decimal
porcentaje_nulos = round((num_ausentes / total_datos) * 100, 1)

print(f'El porcentaje de valores ausentes es del {porcentaje_nulos} %')

# bucle en los encabezados reemplazando los valores ausentes con 'unknown'
columns_to_replace = ['track', 'artist', 'genre'] # lista con los nombres de columnas con valores ausentes

for col in columns_to_replace:
    df[col].fillna('unknown', inplace= True)


# Asegurar de que la tabla no contiene más valores ausentes. Cuenta de nuevo los valores ausentes.

# contando valores ausentes
df.isna().sum()

# Encuentrar el número de duplicados explícitos en la tabla usando un comando:

# contar duplicados explícitos
# uso del método duplicated() con sum()
df.duplicated().sum()


# %%
# eliminar duplicados explícitos
# con el método drop_duplicates eliminar los duplicados y especificar inplace=True para que se guarden los cambios en df
df = df.drop_duplicates().reset_index(drop=True)

# Contar los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# comprobación de duplicados
df.duplicated().sum()

# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. 
# Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero imprimamos una lista de nombres de género únicos, ordenados en orden alfabético. Para hacerlo:
# * se recupera la columna deseada del dataFrame;
# * se llama al método que te devolverá todos los valores de columna únicos;
# * se aplica un método de ordenamiento a tu resultado.

# inspeccionar los nombres de género únicos
# se crea la variable genre_list para guardar los valores únicos
genre_list = df['genre'].unique()

# Se ordena la lista en orden alfabético con el método .sort()
genre_list.sort()

# con un bucle for se muestran los nombres de géneros únicos ordenados
for genre in genre_list:
    print(genre)

# Buscar en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Se verán los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para eliminarlos, se declara la función `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=` — la lista de duplicados;
# * `correct_genre=` — el string con el valor correcto.
# 
# La función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplaza cada valor de la lista `wrong_genres` con el valor en `correct_genre`. Utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos y reemplazarlos con el género correcto en la lista principal.

# función para reemplazar duplicados implícitos
def replace_wrong_genres(df, column, wrong_genres, correct_genre):
    # se emplea un bucle for para iterar sobre lal lista con los nombres incorrectos
    for wrong_value in wrong_genres:
        # uso de replace() para cada nombre incorrecto
        df[column] = df[column].replace(wrong_value, correct_genre)
    return df # devuelve el DataFrame con los nombres correctos


# Se llama a `replace_wrong_genres()` y se pasan los argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) 
# y los reemplace por `hiphop`:

# eliminar duplicados implícitos

# se crea la list con los nombres incorrectos (los duplicados)
duplicados = ['hip', 'hop', 'hip-hop']
# variable que se le asigna el nombre correcto
correct_name = 'hiphop'

# se llama a la función replace_wrong_genres
df = replace_wrong_genres(df, 'genre', duplicados, correct_name)

# %%
# comprobación de duplicados implícitos
# se crea la variable genre_list para guardar los valores únicos
genre_list = df['genre'].unique()

# Se ordena la lista en orden alfabético con el método .sort()
genre_list.sort()

# con un bucle for se muestran los nombres de géneros únicos ordenados
for genre in genre_list:
    print(genre)

 
# `Descripción breve de lo que se observó al analizar los duplicados, cómo se abordaron sus eliminaciones y qué resultados se lograron.`
# 
# Primero los datos ausentes se reemplazron con 'unknown', después se eliminaron los datos duplicados que están de forma explícita 
# con el método drop_duplicates(), sin embargo, aún puede haber datos duplicados que están de forma implícita. Por lo tanto, se empleo 
# el método unique() para la columna 'genre' y se asignó el resultado como una lista a una varible, después se ordenaron los datos y mostraron 
# para identificar los valores duplicados. Finalmente se creo una función con cuatro parámetros para que sustituya los valores incorrectos con 
# el nombre del género correcto. De esta manera los datos quedan limpios para su análisis. 

# ## Etapa 3. Prueba de hipótesis

# ### Hipótesis 1: comparar el comportamiento del usuario en las dos ciudades <a id='activity'></a>

# La primera hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y 
# Shelbyville consumen música. Para comprobar esto, se usan los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Se agrupan a los usuarios y las usuarias por ciudad.
# * Comparar el número de pistas que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Se realiza cada cálculo por separado.
# 
# El primer paso es evaluar la actividad del usuario en cada ciudad. Agrupar los datos por ciudad y encuentrar el 
# número de canciones reproducidas en cada grupo.

# contando las pistas reproducidas en cada ciudad
df.groupby('city')['track'].count() 

# Observaciones 
# En la ciudad de Springfield se reprodujeron más del doble de canciones que en Shelbyville

# Ahora se agrupan los datos por día de la semana y se encuentran el número de pistas reproducidas el lunes, el miércoles y el viernes.

# Cálculo de las pistas reproducidas cada día de la semana
df.groupby('day')['track'].count()

# Observaciones:
# Los días viernes y lunes se reproducen más canciones y en la ciudad de Springfield se reproducen más canciones que en la ciudad de Shelbyville.


# Ahora se necesita escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crear la función `number_tracks()` para calcular el número de canciones reproducidas en un determinado día **y** ciudad. 
# La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'`.
# - `city`: ciudad: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, se aplica un filtrado consecutivo con indexación lógica.
# 
# Primero se filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, se cuenta el número de valores de la columna 'user_id' en la tabla resultante. 
# Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# crear la función number_tracks()
# declararemos la función con dos parámetros: day=, city=.

# deja que la variable track_list almacene las filas df en las que
# el valor del nombre de la columna ‘day’ sea igual al parámetro day= y, al mismo tiempo,
# el valor del nombre de la columna ‘city’ sea igual al parámetro city= (aplica el filtrado consecutivo
# con indexación lógica)
# deja que la variable track_list_count almacene el número de valores de la columna 'user_id' en track_list
# (igual al número de filas en track_list después de filtrar dos veces).
# permite que la función devuelva un número: el valor de track_list_count.

# la función cuenta las pistas reproducidas en un cierto día y ciudad.
# primero recupera las filas del día deseado de la tabla,
# después filtra las filas de la ciudad deseada del resultado,
# luego encuentra el número de pistas en la tabla filtrada,
# y devuelve ese número.
# para ver lo que devuelve, envuelve la llamada de la función en print().


# empieza a escribir tu código aquí
def number_tracks(df,day, city, col1= 'day', col2= 'city'): # se asignan dos parámetros predeterminados col 1 y col2, que tienen el nombre de la columna 'day' y 'city', respectivamente
    track_list = df[df[col1] == day] # primero se filtra por el día
    track_list = track_list[track_list[col2] == city] # después se filtra por la ciudad
    # Se contabilizan el número de valores de la columna 'user_id' después de aplicar los filtros
    track_list_count = track_list['user_id'].count()
    return track_list_count # se devuelve el resultado del conteo 


# Llamar a `number_tracks()` seis veces, cambiando los valores de los parámetros, para que recuperes los datos de ambas ciudades 
# para cada uno de los tres días.

# el número de canciones reproducidas en Springfield el lunes
print(number_tracks(df, 'Monday', 'Springfield'))

# el número de canciones reproducidas en Shelbyville el lunes
print(number_tracks(df, 'Monday', 'Shelbyville'))

# el número de canciones reproducidas en Springfield el miércoles
print(number_tracks(df, 'Wednesday', 'Springfield'))

# el número de canciones reproducidas en Shelbyville el miércoles
print(number_tracks(df, 'Wednesday', 'Shelbyville'))

# el número de canciones reproducidas en Springfield el viernes
print(number_tracks(df, 'Friday', 'Springfield'))

# el número de canciones reproducidas en Shelbyville el viernes
print(number_tracks(df, 'Friday', 'Shelbyville'))

# Utilizar `pd.DataFrame` para crear una tabla, donde
# * los encabezados de la tabla son: `['city', 'monday', 'wednesday', 'friday']`
# * Los datos son los resultados que se conseguieron de `number_tracks()`

# tabla con los resultados
encabezados = ['city', 'monday', 'wednesday', 'friday']
datos =[
    ['Springfield', 15740, 11056, 15945],
    ['Shelbyville', 5614, 7003, 5895]
]

df_number_tracks = pd.DataFrame(data= datos, columns= encabezados)
df_number_tracks


# **Conclusiones**
# 
# `Comentar si la primera hipótesis es correcta o debe rechazarse. Explicar el razonamiento`
# 
# La hipótesis es correcta, ya que si se observan diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville 
# consumen música. En la ciudad de Springfield se escuchan un mayor número de canciones en los tres días, siendo el lunes y el viernes con 
# el mayor número de reproduccioes. Mientras que, en la ciudad de Shelbyville el día miércoles se reproducen un mayor número de canciones. 

# Posiblemente la ciudad de Springfield tiene un mayor número de población que usa la plataforma, se tendrían que solicitar los datos del 
# número de la población por ciudad que usa la plataforma. Otra razón podría ser que los usuarios y usuarias de Springfield tienen un plan 
# premium o mayor poder aquisitivo (o mayores ingresos) por ello pueden permitirse pagar la plataforma de música, para esto último serían 
# necesarios los datos de los sueldos o el tipo de empleo de los usuarios y usuarias para analizar si existe alguna relación.


# ### Hipótesis 2: música al principio y al final de la semana 
# Según la segunda hipótesis, el lunes por la mañana y el viernes por la noche, los ciudadanos de Springfield escuchan géneros que 
# difieren de los que disfrutan los usuarios de Shelbyville.

# Crear dos tablas con los nombres proporcionados en los dos bloques de código a continuación:
# * Para Springfield — `spr_general`
# * Para Shelbyville — `shel_general`

# crear la tabla spr_general a partir de las filas df
# donde los valores en la columna 'city' es 'Springfield'
spr_general = df[df['city'] == 'Springfield']

# crear la tabla shel_general a partir de las filas df
# donde los valores en la columna 'city' es 'Shelbyville'
shel_general = df[df['city'] == 'Shelbyville']

# Escribir la función `genre_weekday()` con cuatro parámetros:
# * Una tabla para los datos (`df`)
# * El día de la semana (`day`)
# * La marca de fecha y hora en formato 'hh:mm:ss' (`time1`)
# * La marca de fecha y hora en formato 'hh:mm:ss' (`time2`)
# 
# La función debe devolver los 15 géneros más populares en un día específico dentro del período definido por las dos marcas de tiempo, junto con sus respectivos recuentos de reproducción.
# Aplica la misma lógica de filtrado consecutiva, pero usa cuatro filtros esta vez y luego crea una nueva columna con los recuentos de reproducción respectivos.
# Ordena el resultado de un recuento más grande a uno más pequeño y devuélvelo.

# 1) Deja que la variable genre_df almacene las filas que cumplen varias condiciones:
#    - el valor de la columna 'day' es igual al valor del argumento day=
#    - el valor de la columna 'time' es mayor que el valor del argumento time1=
#    - el valor en la columna 'time' es menor que el valor del argumento time2=
#    Utiliza un filtrado consecutivo con indexación lógica.

# 2) Agrupa genre_df por la columna 'genre', toma una de sus columnas,
#    y utiliza el método size() para encontrar el número de entradas por cada uno de
#    los géneros representados; almacena los Series resultantes en
#    la variable genre_df_count

# 3) Ordena genre_df_count en orden descendente de frecuencia y guarda el resultado
#    en la variable genre_df_sorted

# 4) Devuelve un objeto Series con los primeros 15 valores de genre_df_sorted - los 15
#    géneros más populares (en un determinado día, en un determinado periodo de tiempo)

# la función es:
def genre_weekday(df, day, time1, time2):
    # filtrado consecutivo
    # Crea la variable genre_df que almacenará solo aquellas filas df donde el día es igual a day=
    genre_df = df[df['day'] == day] # escribe tu código aquí

    # Filtra genre_df nuevamente para almacenar solo las filas donde el tiempo es menor que time2=
    genre_df = genre_df[genre_df['time'] < time2] # escribe tu código aquí

    # Filtra genre_df una vez más para almacenar solo las filas donde el tiempo es mayor que time1=
    genre_df = genre_df[genre_df['time'] > time1] # escribe tu código aquí

    # Agrupa el DataFrame filtrado por la columna con los nombres de los géneros, selecciona la columna 'genre',
    # y encuentra el número de filas para cada género con el método count()
    genre_df_count = genre_df.groupby('genre')['genre'].count() # escribe tu código aquí

    # Ordenaremos el resultado en orden descendente (por lo que los géneros más populares aparecerán primero en el objeto Series)
    genre_df_sorted = genre_df_count.sort_values(ascending= False) # escribe tu código aquí

    # Devuelve un objeto de Series con los primeros 15 valores de genre_df_sorted: los 15 géneros más populares (en un día determinado, dentro de un período de timeframe)
    return genre_df_sorted[:15]

# Comparar los resultados de la función `genre_weekday()` para Springfield y Shelbyville el lunes por la mañana (de 7 a 11) y 
# el viernes por la tarde (de 17:00 a 23:00). Utiliza el mismo formato de hora de 24 horas que el conjunto de datos (por ejemplo, 05:00 = 17:00:00):

# llamando a la función para el lunes por la mañana en Springfield (utilizando spr_general en vez de la tabla df)
spr_morning = genre_weekday(spr_general, 'Monday', '07:00:00', '11:00:00')
spr_morning # se guarda el resultado en una variable


# Se guarda una lista del top 15 de los géneros más populares en Sprinfield del día lunes por la mañana.

spr_morning_list = spr_morning.keys() #se emplea el método keys() para guardar los géneros como una lista
spr_morning_list

# llamando a la función para el lunes por la mañana en Shelbyville (utilizando shel_general en vez de la tabla df)
shel_morning = genre_weekday(shel_general, 'Monday', '07:00:00', '11:00:00')
shel_morning # se guarda el resultado en una variable

# Se guarda una lista del top 15 de los géneros más populares en Shelbyville del día lunes por la mañana.

shel_morning_list = shel_morning.keys()
shel_morning_list

# De la misma manera, el resultado al llamar la función genre_weekday() se guarda en una variable para los resultados del viernes por la noche para cada ciudad.

# llamando a la función para el viernes por la tarde en Springfield
spr_night = genre_weekday(spr_general, 'Friday', '17:00:00', '23:00:00')
spr_night

spr_night_list = spr_night.keys() #se emplea el método keys() para guardar los géneros como una lista
spr_night_list

# llamando a la función para el viernes por la tarde en Shelbyville
shel_night = genre_weekday(shel_general, 'Friday', '17:00:00', '23:00:00')
shel_night

shel_night_list = shel_night.keys() #se emplea el método keys() para guardar los géneros como una lista
shel_night_list


# **Se crea una función con un bucle *for* para comparar los géneros que coinciden por la mañana del día lunes y en la noche del 
# día viernes en ambas ciudades. Los géneros que coinciden se guardan en la lista morn_genres_equal y los que no coinciden en la 
# variable morn_genres_no_equal**



# Se crea la función con dos parámetros, que será la lista 1 que se desean comparar con lalista 2
def genres_equals(genre_list1, genre_list2):
    # Se crea la variable con una lista vacia en donde se guardaran los géneros que coincidan de las lista 1 con los géneros de la lista 2
    genres_equal = [] 
    genres_no_equal = [] # Se crea la variable con una lista vacia en donde se guardaran los géneros que no coincidan
    
    # Se itera sobre la lista 1 con los nombres de los géneros
    for genre in genre_list1:
            # Se comprueba si los géneros de la lista 1 se encuentran en la lista 2 de géneros 
            if genre in genre_list2: 
                # Si el género de la lista 1 coincide con el genéro de la lista 2, se guarda en la variable genres_equal
                genres_equal.append(genre) 
            else:
                genres_no_equal.append(genre) # Si el género de la lista 1 no coincide con el genéro de la lista 2, se guarda en la variable genres_no_equal
                
    return genres_equal, genres_no_equal # Se devuelve el resultado de las listas genres_equal, genres_no_equal
            

# Géneros que coinciden el lunes por la mañana de la ciudad Springfield con la ciudad de Shebyville

# Se comparan los géneros que coinciden el lunes por la mañana de Springfield con Shebyville
morning_equals , morning_no_equals = genres_equals(spr_morning_list, shel_morning_list)

# La variable morning_equals guarda los géneros de la ciudad Springfield que coinciden con los géneros de las ciudad de Shebyville
print(f'Géneros del lunes por la mañana de Springfield que coinciden con los géneros de Shelbyville:\n{morning_equals}')
print()
print(f'Géneros del lunes por la mañana de Springfield que no coinciden con los géneros de Shelbyville:\n{morning_no_equals}')

# Géneros que coinciden el viernes por la noche de la ciudad Springfield con la ciudad de Shebyville

# Se comparan los géneros que coinciden el viernes por la noche de Springfield con Shelbyville
night_equals , night_no_equals = genres_equals(spr_night_list, shel_night_list)
print(f'Géneros del viernes por la noche de Springfield que coinciden con los géneros de Shelbyville:\n{night_equals}')
print()
print(f'Géneros del viernes por la noche Springfield que no coinciden con los géneros de Shelbyville:\n{night_no_equals}')

# **Conclusiones**
# 
# `Comentar si la segunda hipótesis es correcta o debe rechazarse. Explica el razonamiento.`
# 
# La hipotesis se rechaza parcialmente, ya que los géneros escuchados por los y las habitantes de Springfield no difieren de los géneros 
# que se escuchan en Shelbyville. El lunes por la mañana 13 géneros que se escuchan en la ciudad de Springfield coinciden (`morning_equals`) 
# con los géneros que se escuchan en Shelbyville, unicamente dieren dos géneros. Además, los dos géneros más escuchados en ambas ciudades son 
# el pop y el dance.
# 
# De la misma manera el viernes por la noche los géneros escuchados en la ciudad de Springfield no difieren de los géneros que se escuchan 
# Shelbyville. De los géneros de Springfield son 14 los que coinciden (`night_equals`) con los géneros de la ciudad de Shelbyville, además, 
# los dos géneros más escuchados en las dos ciudades son el pop y el rock. 


# ### Hipótesis 3: preferencias de género en Springfield y Shelbyville <a id='genre'></a>
# 
# Hipótesis: Shelbyville ama la música rap. A los residentes de Springfield les gusta más el pop.

# Agrupar la tabla `spr_general` por género y encuentra el número de canciones reproducidas de cada género con el método `count()`. 
# Luego ordenar el resultado en orden descendente y guárdarlo en la variable `spr_genres`.

# escribir una línea de código que:
# 1. agrupe la tabla spr_general por la columna 'genre';
# 2. cuente los valores 'genre' con count() en la agrupación;
# 3. ordene el Series resultante en orden descendente y lo guarde en spr_genres.
spr_genres = spr_general.groupby('genre')['genre'].count().sort_values(ascending= False)


# muestra los primeros 10 valores de spr_genres
spr_genres[:10]

# Ahora  lo mismo con los datos de Shelbyville.
# 
# Agrupar la tabla `shel_general` por género y encuentra el número de canciones reproducidas de cada género. 
# Después, ordenar el resultado en orden descendente y guárdalo en la tabla `shel_genres`:

# escribir una línea de código que:
# 1. agrupe la tabla shel_general por la columna 'genre';
# 2. cuente los valores 'genre' con count() en la agrupación;
# 3. ordene el Series resultante en orden descendente y lo guarde en shel_genres.
shel_genres = shel_general.groupby('genre')['genre'].count().sort_values(ascending= False)

# imprimir las 10 primeras filas de shel_genres
shel_genres[:10]

# **Conclusión**
# 
# `Comentar si la tercera hipótesis es correcta o debe rechazarse. Explica el razonamiento.`
# 
# La hipótesis debe aceptarse parcialmente, ya que en la ciudad de Springfield el género más escuchado si es el pop. 
# Mientras que en la ciudad de Shelbyville el rap no es el género más escuchado por los usarios y usuarias, también es el pop 
# el género preferido. Un punto importante a resaltar es que en la ciudad de Springfield el número de canciones reproducidas de 
# pop es más del doble de las canciones pop reproducidas en Shelbyville. Por otro lado, el género rap no aparece en el top 10 de 
# los géneros más escuchados de ambas ciudades.

# # Conclusiones 

# `Resumen de conclusiones sobre cada hipótesis aquí`
# 
# El comportamiento del consumo de música de los usuarios y las usuarias en las ciudades de Springfield y Shelbyville si es diferente, 
# ya que depende del día de la semana. Además, en general hay un mayor número de reproducciones de canciones en Springfield.
# 
# Los géneros más escuchados el lunes por la mañana y el viernes por la noche, no son muy diferentes entre ambas ciudades, ya que se 
# escuchan los mismos géneros en dichos horarios y días.
# 
# El género más escuchado en las dos ciudades es el pop, siendo la ciudad de Springfield la que tiene mayor número de canciones pop 
# reproducidas.



