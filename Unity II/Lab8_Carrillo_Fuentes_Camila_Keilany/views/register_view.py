import tkinter as tk
from tkinter import messagebox


class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)

        self.ventana.title("Registro de Usuarios")

        self.ventana.geometry("440x480")

        self.ventana.configure(bg="#AEADAF")

        self.ventana.resizable(False, False)
        self.ventana.transient(root)
        self.ventana.grab_set()

        self.titulo = tk.Label(
            self.ventana,
            text="CREAR CUENTA",
            font=("Helvetica", 18, "bold"),
            bg="#D3B9E9",
            fg="#583B7E"
        )
        self.titulo.pack(pady=18)

        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Nombre completo:",
            bg="#D3B9E9",
            font=("Helvetica", 10, "bold"),
            fg="#583B7E"
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=35,
            font=("Helvetica", 10)
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_email = tk.Label(
            self.ventana,
            text="Correo electrónico:",
            bg="#D3B9E9",
            font=("Helvetica", 10, "bold"),
            fg="#583B7E"
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            self.ventana,
            width=35,
            font=("Helvetica", 10)
        )
        self.entry_email.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Contraseña:",
            bg="#D3B9E9",
            font=("Helvetica", 10, "bold"),
            fg="#583B7E"
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana,
            width=35,
            show="*",
            font=("Helvetica", 10)
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirmar contraseña:",
            bg="#D3B9E9",
            font=("Helvetica", 10, "bold"),
            fg="#583B7E"
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=35,
            show="*",
            font=("Helvetica", 10)
        )
        self.entry_confirmar.pack(pady=4)

        self.btn_guardar = tk.Button(
            self.ventana,
            text="Registrar usuario",
            width=22,
            bg="#583B7E",
            fg="white",
            font=("Helvetica", 10, "bold"),
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=12)

        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=22,
            bg="#5C0900",
            fg="white",
            font=("Helvetica", 10, "bold"),
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()

        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(
                titulo,
                mensaje,
                parent=self.ventana
            )
        else:
            messagebox.showinfo(
                titulo,
                mensaje,
                parent=self.ventana
            )

    def cerrar(self):
        self.ventana.destroy()