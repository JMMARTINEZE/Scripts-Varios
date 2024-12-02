import tkinter as tk
from tkinter import messagebox
import subprocess

class InventarioApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inventario de Ansible")

        # Crear etiquetas y campos de texto para la IP, usuario y contraseña
        tk.Label(self.root, text="IP:").grid(row=0, column=0)
        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Usuario:").grid(row=1, column=0)
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Contraseña:").grid(row=2, column=0)
        self.contraseña_entry = tk.Entry(self.root, show="*")
        self.contraseña_entry.grid(row=2, column=1)

        # Crear botón para generar el inventario
        tk.Button(self.root, text="Generar inventario", command=self.generar_inventario).grid(row=3, column=0, columnspan=2)

    def generar_inventario(self):
        ip = self.ip_entry.get()
        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()

        # Crear un archivo de secretos utilizando Ansible Vault
        subprocess.run(["ansible-vault", "create", "secrets.yml"])

        # Agregar la contraseña al archivo de secretos
        with open("secrets.yml", "a") as f:
            f.write(f"contraseña: {contraseña}\n")

        # Cifrar el archivo de secretos
        subprocess.run(["ansible-vault", "encrypt", "secrets.yml"])

        # Generar el archivo de inventario de Ansible
        with open("inventario.yml", "w") as f:
            f.write(f"""
            all:
              hosts:
                - cliente
              children:
                clientes:
                  hosts:
                    cliente:
                      ansible_host: {ip}
                      ansible_user: {usuario}
                      ansible_password: !vault
                        $ANSIBLE_VAULT;1.1;AES256
                        {subprocess.check_output(["ansible-vault", "view", "secrets.yml"]).decode().strip()}
            """)

        # Mostrar un mensaje de confirmación
        messagebox.showinfo("Inventario generado", "El archivo de inventario ha sido generado correctamente.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = InventarioApp()
    app.run()