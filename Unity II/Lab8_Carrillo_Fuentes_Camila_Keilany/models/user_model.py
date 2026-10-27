import psycopg
from controllers.conexion_controller import Conexion


class UserModel:

    def __init__(self):
        self.conexion_db = Conexion()

    def registrar_usuario(self, nombre, email, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return "error"

        cursor = None

        try:
            cursor = conexion.cursor()

            # Obtener el id máximo actual para asignarlo manualmente
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM login_mvc.users")
            siguiente_id = cursor.fetchone()[0]

            consulta = """
                INSERT INTO login_mvc.users (id, nombre, email, pass)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(consulta, (siguiente_id, nombre, email, password))
            conexion.commit()

            return "ok"

        except psycopg.errors.UniqueViolation:
            return "duplicado"

        except psycopg.Error as error:
            print("--> Error de PostgreSQL al registrar usuario:", error)
            return "error"

        except Exception as error:
            print("--> Error inesperado al registrar usuario:", error)
            return "error"

        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                conexion.close()

    def validar_usuario(self, email, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return None

        cursor = None

        try:
            cursor = conexion.cursor()

            consulta = """
                SELECT id, nombre
                FROM login_mvc.users
                WHERE email = %s AND pass = %s
            """

            cursor.execute(consulta, (email, password))
            usuario = cursor.fetchone()

            if usuario:
                if isinstance(usuario, dict):
                    return usuario['id'], usuario['nombre']
                return usuario[0], usuario[1]

            return None

        except Exception as error:
            print("--> Error al validar usuario:", error)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                conexion.close()

    def cerrar(self):
        pass