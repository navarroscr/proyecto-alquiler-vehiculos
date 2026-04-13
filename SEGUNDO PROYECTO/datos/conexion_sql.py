import pyodbc

SERVIDOR = "localhost"
BASE_DATOS = "autotrust"


def obtener_conexion():
    """
    Conecta a SQL Server usando Windows Authentication.
    Retorna el objeto de conexión.
    """
    try:
        conexion = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={SERVIDOR};"
            f"DATABASE={BASE_DATOS};"
            f"Trusted_Connection=yes;"
        )
        return conexion
    except pyodbc.Error as e:
        print(f"Error al conectar a SQL Server: {e}")
        raise

if __name__ == "__main__":
    conn = obtener_conexion()
    print("Conexión exitosa a SQL Server")
    conn.close()