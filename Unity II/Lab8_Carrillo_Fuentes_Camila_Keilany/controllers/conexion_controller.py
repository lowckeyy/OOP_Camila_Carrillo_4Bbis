import psycopg
from psycopg.rows import dict_row
from controllers.config import db_config


class Conexion:

    def __init__(self):
        self.config = db_config

    def conectar(self):
        try:
            conexion = psycopg.connect(
                host=self.config.get('host', 'localhost'),
                user=self.config.get('user', 'postgres'),
                password=str(self.config.get('password', '')),
                dbname=self.config.get('database', 'postgres'),
                port=self.config.get('port', 5432)
            )
            return conexion
        except Exception as e:
            print(f"Error al conectar con PostgreSQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
        conexion = self.conectar()
        if not conexion:
            return None

        try:
            with conexion.cursor(row_factory=dict_row) as cursor:
                cursor.execute(query, params)
                resultados = cursor.fetchall()
                return resultados
        except Exception as e:
            print(f"Error al ejecutar consulta SQL: {e}")
            return None
        finally:
            if conexion:
                conexion.close()