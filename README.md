# Proyecto de Gestión de Depósitos Bancarios

Este proyecto permite mantener un registro detallado de depósitos y fondos en instituciones financieras y calcular proyecciones de rendimientos generados. La aplicación se desarrolla en Python y utiliza SQLite para la gestión de la base de datos.

## Requisitos

- Python 3.8+
- SQLite

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crear y poblar la base de datos:
    ```bash
    sqlite3 bancos.db < schema.sql
    ```

## Uso

### Gestión de Instituciones

El script `crud.py` permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en las instituciones financieras.

#### Crear una Institución

```bash
python crud.py institucion crear NOMBRE [-s {0,1}] [-d DESCRIPCION]
```

#### Leer una Institución

```bash
python crud.py institucion leer NOMBRE
```

#### Actualizar una Institución

```bash
python crud.py institucion actualizar NOMBRE [-s {0,1}] [-d DESCRIPCION]
```

#### Eliminar una Institución

```bash
python crud.py institucion eliminar NOMBRE
```

### Gestión de Depósitos

El script `crud.py` también permite realizar operaciones CRUD en los depósitos.

#### Crear un Depósito

```bash
python crud.py deposito crear NOMBRE [-d DESCRIPCION] [-m MONTO] [-t TASA_INTERES]
```

#### Leer un Depósito

```bash
python crud.py deposito leer NOMBRE
```

#### Actualizar un Depósito

```bash
python crud.py deposito actualizar NOMBRE [-d DESCRIPCION] [-m MONTO] [-t TASA_INTERES]
```

#### Eliminar un Depósito

```bash
python crud.py deposito eliminar NOMBRE
```

### Herramientas de Consulta

El script `helper.py` proporciona herramientas de consulta adicionales para la base de datos de bancos.

#### Obtener Sumatoria de Depósitos

```bash
python helper.py suma
```

#### Obtener Proyección de Rendimientos

```bash
python helper.py proyeccion
```

## Estructura del Proyecto

- **crud.py**: Script para realizar operaciones CRUD en instituciones y depósitos.
- **helper.py**: Script para herramientas de consulta adicionales.
- **schema.sql**: Script SQL para crear la base de datos y sus tablas.
- **bancos.db**: Base de datos SQLite (generada después de ejecutar el script SQL).
