import tkinter as tk
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.auth_controller import Authentication


def main():
    root = tk.Tk()

    modelo = UserModel()
    vista = LoginView(root)
    controlador = Authentication(modelo, vista)

    root.mainloop()


if __name__ == "__main__":
    main()