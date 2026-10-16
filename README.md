# Generación Masiva de Personas con Python y SQLAlchemy

## 1. Descripción del proyecto

Este proyecto permite generar e insertar registros de personas en una base de datos MySQL utilizando **Python, SQLAlchemy y Faker**.

El programa crea automáticamente la tabla de personas si no existe, permite insertar un registro manualmente y genera **100.000 registros ficticios** mediante Faker.

Para mejorar el rendimiento, los registros se insertan por lotes de 1.000, evitando realizar una transacción independiente por cada persona.

### Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **SQLAlchemy:** ORM para gestionar las operaciones con la base de datos.
- **Faker:** biblioteca para generar datos ficticios.
- **MySQL:** sistema gestor de base de datos.
- **PyMySQL:** controlador para conectar Python con MySQL.
- **python-dotenv:** permite cargar variables de entorno desde un archivo `.env`.
- **DBeaver:** herramienta opcional para visualizar y administrar los registros almacenados.

## 2. Funcionalidades

El programa permite:

1. Conectarse a MySQL mediante variables de entorno.
2. Crear la tabla de personas automáticamente si no existe.
3. Insertar una persona manualmente.
4. Generar 100.000 registros ficticios con Faker.
5. Insertar los registros por lotes para optimizar el rendimiento.
6. Evitar correos electrónicos duplicados utilizando identificadores únicos.
7. Consultar y mostrar el número total de personas almacenadas.

Los datos generados incluyen nombre, apellido, edad, correo electrónico, teléfono, dirección, profesión, ciudad y género.

## 3. Requisitos previos

Para ejecutar el proyecto es necesario contar con:

- Python instalado.
- MySQL instalado y en funcionamiento, o acceso a un servidor MySQL.
- Una base de datos creada en MySQL.
- Acceso a una terminal, como PowerShell o CMD.

## 4. Instalación

### Paso 1. Obtener el proyecto

Clonar el repositorio desde GitHub:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta del proyecto:

```bash
cd Actividad_3
```

### Paso 2. Crear el entorno virtual

Ejecutar:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

### Paso 3. Instalar las dependencias

Instalar todas las bibliotecas necesarias mediante el archivo `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Las dependencias principales son:

```text
SQLAlchemy
Faker
python-dotenv
PyMySQL
```

## 5. Configuración de la base de datos

Crear una base de datos en MySQL:

```sql
CREATE DATABASE actividad_3;
```

En la raíz del proyecto, crear un archivo llamado `.env` con la siguiente configuración:

```dotenv
DATABASE_URL=mysql+pymysql://USUARIO:CONTRASENA@localhost:3306/actividad_3

TOTAL_PERSONAS=100000
BATCH_SIZE=1000
FAKER_LOCALE=es_CO
```

**Descripción de las variables:**

| Variable | Descripción |
|---|---|
| DATABASE_URL | URL de conexión a MySQL. |
| TOTAL_PERSONAS | Cantidad de personas que se generarán. |
| BATCH_SIZE | Cantidad de registros insertados por lote. |
| FAKER_LOCALE | Configuración regional de Faker. |

Reemplazar `USUARIO` y `CONTRASENA` por las credenciales correspondientes. Si la contraseña contiene caracteres especiales, deben codificarse correctamente para utilizarla dentro de una URL.

**Importante:** no subir el archivo `.env` a GitHub, ya que puede contener información sensible.

## 6. Ejecutar el programa

Una vez configurada la conexión y las dependencias, abrir una terminal en la carpeta principal del proyecto y ejecutar:

```bash
python main.py
```

El programa realizará automáticamente las siguientes operaciones:

1. Establecer la conexión a MySQL.
2. Crear la tabla si todavía no existe.
3. Insertar una persona manualmente.
4. Generar e insertar 100.000 personas ficticias.
5. Consultar la cantidad total de registros.

### Ejemplo de salida

```text
Tabla personas preparada.
Persona individual creada con ID: 1

Insertados 1000 de 100000 registros
Insertados 2000 de 100000 registros
Insertados 3000 de 100000 registros
...
Insertados 99000 de 100000 registros
Insertados 100000 de 100000 registros

Total de personas en la BD: 100001
```

El resultado de 100.001 registros corresponde a una persona insertada manualmente y 100.000 generadas mediante Faker, suponiendo que la base de datos estaba vacía.

## 7. Verificar los resultados

Los registros pueden visualizarse desde DBeaver o cualquier cliente compatible con MySQL.

Para conocer la cantidad de registros almacenados:

```sql
SELECT COUNT(*) FROM personas;
```

Para consultar los primeros 100 registros:

```sql
SELECT *
FROM personas
LIMIT 100;
```

El nombre de la tabla debe coincidir con el definido en `__tablename__` dentro del modelo SQLAlchemy.

## 8. Consideraciones importantes

- La base de datos MySQL debe existir antes de ejecutar el programa.
- SQLAlchemy crea la tabla automáticamente cuando no existe.
- Faker genera información ficticia, no datos reales de personas.
- Las inserciones se realizan por lotes para reducir el número de transacciones.
- Si se ejecuta nuevamente el programa, se añadirán nuevos registros sin eliminar los anteriores.
- Es recomendable utilizar variables de entorno para mantener las credenciales fuera del código fuente.

---

**Proyecto desarrollado con Python, SQLAlchemy, Faker y MySQL.**