import argparse
import sqlite3

def conectar_db():
    return sqlite3.connect('bancos.db')

def crear_institucion(nombre, es_sofipo, descripcion):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Institucion VALUES (?, ?, ?)", (nombre, es_sofipo, descripcion))
    conn.commit()
    conn.close()
    print(f"Institución '{nombre}' creada con éxito.")

def leer_institucion(nombre):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Institucion WHERE sNombre = ?", (nombre,))
    row = cursor.fetchone()
    conn.close()
    if row:
        print(f"Institución: {row[0]}, Es SOFIPO: {row[1]}, Descripción: {row[2]}")
    else:
        print(f"Institución '{nombre}' no encontrada.")

def actualizar_institucion(nombre, es_sofipo, descripcion):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Institucion SET bSofipo = ?, sDescripcion = ? WHERE sNombre = ?", (es_sofipo, descripcion, nombre))
    conn.commit()
    conn.close()
    print(f"Institución '{nombre}' actualizada con éxito.")

def eliminar_institucion(nombre):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Institucion WHERE sNombre = ?", (nombre,))
    conn.commit()
    conn.close()
    print(f"Institución '{nombre}' eliminada con éxito.")

# ... (Funciones CRUD similares para la tabla Deposito)
def crear_deposito(nombre:str, desc:str ='', monto:float =0, tasa_interes_anual:float =0):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Deposito (sNombre, nIdInstitucion, sDescripcion, nMonto, nTasaInteresAnual) VALUES (?, ?, ?, ?, ?)", (nombre, desc, monto, tasa_interes_anual))
    conn.commit()
    conn.close()
    print(f"Deposito '{nombre}' creado con éxito.")

def leer_deposito(nombre:str):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Deposito WHERE sNombre = ?", (nombre,))
    row = cursor.fetchone()
    conn.close()
    if row:
        print(f"Deposito: {row[0]}, Descripción: {row[1]}, Monto: {row[2]}, Tasa de Interés Anual: {row[3]}")
    else:
        print(f"Deposito '{nombre}' no encontrado.")

def actualizar_deposito(nombre:str, desc:str ='', monto:float =0, tasa_interes_anual:float =0):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Deposito SET sDescripcion = ?, nMonto = ?, nTasaInteresAnual = ? WHERE sNombre = ?", (desc, monto, tasa_interes_anual, nombre))
    conn.commit()
    conn.close()
    print(f"Deposito '{nombre}' actualizado con éxito.")

def eliminar_deposito(nombre:str):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Deposito WHERE sNombre = ?", (nombre,))
    conn.commit()
    conn.close()
    print(f"Deposito '{nombre}' eliminado con éxito.")

def main():
    parser = argparse.ArgumentParser(description="CRUD para la base de datos de ")

    subparsers = parser.add_subparsers(dest="tabla")

    # Subparser para Institucion
    inst_parser = subparsers.add_parser("institucion", help="Operaciones CRUD para instituciones")
    inst_parser.add_argument("operacion", choices=["crear", "leer", "actualizar", "eliminar"], help="Operación a realizar")
    inst_parser.add_argument("nombre", help="Nombre de la institución")
    inst_parser.add_argument("-s", "--sofipo", type=int, choices=[0, 1], help="Es SOFIPO (1 para Sí, 0 para No)")
    inst_parser.add_argument("-d", "--descripcion", help="Descripción de la institución")

    # Subparser para Deposito (similar al de Institucion)
    dep_parser = subparsers.add_parser("deposito", help="Operaciones CRUD para depósitos")
    dep_parser.add_argument("operacion", choices=["crear", "leer", "actualizar", "eliminar"], help="Operación a realizar")
    dep_parser.add_argument("nombre", help="Nombre del depósito")
    dep_parser.add_argument("-d", "--descripcion", help="Descripción del depósito")
    dep_parser.add_argument("-m", "--monto", type=float, help="Monto del depósito")
    dep_parser.add_argument("-t", "--tasa_interes", type=float, help="Tasa de interés anual del depósito")

    args = parser.parse_args()

    if args.tabla == "institucion":
        if args.operacion == "crear":
            crear_institucion(args.nombre, args.sofipo, args.descripcion)
        elif args.operacion == "leer":
            leer_institucion(args.nombre)
        elif args.operacion == "actualizar":
            actualizar_institucion(args.nombre, args.sofipo, args.descripcion)
        elif args.operacion == "eliminar":
            eliminar_institucion(args.nombre)
        else:
            parser.print_help()

    elif args.tabla == "deposito":
        if args.operacion == "crear":
            crear_deposito(args.nombre, args.descripcion, args.monto, args.tasa_interes)
        elif args.operacion == "leer":
            leer_deposito(args.nombre)
        elif args.operacion == "actualizar":
            actualizar_deposito(args.nombre, args.descripcion, args.monto, args.tasa_interes)
        elif args.operacion == "eliminar":
            eliminar_deposito(args.nombre)
        else:
            parser.print_help()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
