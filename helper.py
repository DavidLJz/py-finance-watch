import sqlite3
import argparse
import sys

def obtener_sumatoria_depositos(bancos=None, depositos=None):
    """Obtiene la sumatoria de los depósitos según los filtros."""
    conn = sqlite3.connect('bancos.db')
    cursor = conn.cursor()

    query = "SELECT SUM(nMonto) FROM Deposito"
    filtros = []
    if bancos:
        bancos_str = ",".join(f"'{b}'" for b in bancos)
        filtros.append(f"nIdInstitucion IN ({bancos_str})")
    if depositos:
        depositos_str = ",".join(f"'{d}'" for d in depositos)
        filtros.append(f"sNombre IN ({depositos_str})")
    if filtros:
        query += " WHERE " + " AND ".join(filtros)

    cursor.execute(query)
    resultado = cursor.fetchone()[0]
    conn.close()
    return resultado or 0  # Retorna 0 si no hay resultados

def obtener_proyeccion_rendimientos(bancos=None, depositos=None, periodo=365):
    """Obtiene la proyección de rendimientos en un período dado."""
    conn = sqlite3.connect('bancos.db')
    cursor = conn.cursor()

    query = """
        SELECT SUM(nMonto * nTasaInteresAnual / 100 * ?) / 365
        FROM Deposito
        WHERE nTasaInteresAnual IS NOT NULL
    """
    filtros = []
    if bancos:
        bancos_str = ",".join(f"'{b}'" for b in bancos)
        filtros.append(f"nIdInstitucion IN ({bancos_str})")
    if depositos:
        depositos_str = ",".join(f"'{d}'" for d in depositos)
        filtros.append(f"sNombre IN ({depositos_str})")
    if filtros:
        query += " AND " + " AND ".join(filtros)

    cursor.execute(query, (periodo,))
    resultado = cursor.fetchone()[0]
    conn.close()
    return resultado or 0

def main():
    parser = argparse.ArgumentParser(description="Herramientas de consulta para la base de datos de bancos.")
    subparsers = parser.add_subparsers(dest="comando")

    suma_parser = subparsers.add_parser("suma", help="Obtener sumatoria de depósitos")
    suma_parser.add_argument("-b", "--bancos", nargs="+", help="Lista de bancos a considerar")
    suma_parser.add_argument("-d", "--depositos", nargs="+", help="Lista de depósitos a considerar")

    proyeccion_parser = subparsers.add_parser("proyeccion", help="Obtener proyección de rendimientos")
    proyeccion_parser.add_argument("periodo", type=int, help="Período en días (por defecto 365)")
    proyeccion_parser.add_argument("-b", "--bancos", nargs="+", help="Lista de bancos a considerar")
    proyeccion_parser.add_argument("-d", "--depositos", nargs="+", help="Lista de depósitos a considerar")

    args = parser.parse_args()

    # 2000 -> $2,000.00
    def formatter (n:float) -> str:
        return f"${n:,.2f}"

    if args.comando == "suma":
        resultado = obtener_sumatoria_depositos(args.bancos, args.depositos)
        print(f"La sumatoria de los depósitos es: {formatter(resultado)}")
    elif args.comando == "proyeccion":
        resultado = obtener_proyeccion_rendimientos(args.bancos, args.depositos, args.periodo)
        print(f"La proyección de rendimientos en {args.periodo} días es: {formatter(resultado)}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
