import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import pandas as pd
import os

# Revisar o crear CSV vacío para los datos de servicio
csv_file = "data.csv"
if os.path.exists(csv_file):
    try:
        database = pd.read_csv(csv_file)
        # Si el CSV está vacío (sin columnas), crear columnas
        if database.empty:
            database = pd.DataFrame(columns=["Nombre", "Corte", "Fecha"])
    except pd.errors.EmptyDataError:
        # CSV vacío, crear DataFrame con columnas
        database = pd.DataFrame(columns=["Nombre", "Corte", "Fecha"])
else:
    # Crear CSV nuevo con columnas
    database = pd.DataFrame(columns=["Nombre", "Corte", "Fecha"])
    database.to_csv(csv_file, index=False)
    
# Revisar o crear CSV vacío para la base de datos del cliente
csv_file_register = "data_client.csv"
if os.path.exists(csv_file_register):
    try:
            database_client = pd.read_csv(csv_file_register)
            # Si el CSV está vacío (sin columnas), crear columnas
            if database_client.empty:
                database_client = pd.DataFrame(columns=["Nombre", "Numero telefonico", "Genero", "Fecha"])
    except pd.errors.EmptyDataError:
            # CSV vacío, crear DataFrame con columnas
            database_client = pd.DataFrame(columns=["Nombre", "Numero telefonico", "Genero", "Fecha"])
else:
        # Crear CSV nuevo con columnas
        database_client = pd.DataFrame(columns=["client_ID","Nombre", "Numero telefonico", "Genero", "Fecha"])
        database_client.to_csv(csv_file_register, index=False)

# Ventana principal
root = tk.Tk()
root.title("DYP'S Barber Shop")
root.geometry("1000x900")

# Nombre
tk.Label(root, text="Teléfono").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

# Tipo de servicio
tk.Label(root, text="Tipo de corte:").pack()
combo_corte = ttk.Combobox(root, values=["Corte clásico", "Escolar", "TheDypps", "VIP", "El patrón", "Fleco"])
combo_corte.pack()

def registro():
#Función de registro de clientes nuevos    
#Ventana para registro   
    # Ventana de registro
    root_register = tk.Toplevel(root)
    root_register.title("Registrar cliente nuevo")
    root_register.geometry("500x500")

    # Nombre
    tk.Label(root_register, text="Nombre").pack()
    reg_nombre = tk.Entry(root_register)
    reg_nombre.pack()
    
    # Telefono
    tk.Label(root_register, text="Numero").pack()
    reg_tel = tk.Entry(root_register)
    reg_tel.pack()

    # Genero
    tk.Label(root_register, text="Genero").pack()
    combo_genre = ttk.Combobox(root_register, values=["Hombre", "Mujer"])
    combo_genre.pack()
    
    def guardar_cliente():
        nombre = reg_nombre.get().strip()
        telefono = reg_tel.get().strip()
        genero = combo_genre.get().strip()
        fecha_cliente = pd.Timestamp.today()

        if not nombre or not telefono or not genero or not fecha_cliente:
            messagebox.showwarning("Error", "Ingresa todos los campos, por favor")
            return

        global database_client
        nueva_fila = {"Nombre": nombre, "Numero telefonico": telefono, "Genero": genero, "Fecha": fecha_cliente.date()}
        database_client = pd.concat([database_client, pd.DataFrame([nueva_fila])], ignore_index=True)
        database_client.to_csv(csv_file_register, index=False)

        messagebox.showinfo("Guardado", f"Cliente {nombre} registrado")
        reg_nombre.delete(0, tk.END)
        reg_tel.delete(0, tk.END)
        combo_genre.set("")
        
    #boton guardar cliente
    guardar_cliente_bt= tk.Button(root_register, text="Guardar", command=guardar_cliente)
    guardar_cliente_bt.pack(pady=10)

# Función guardar
def guardar():
    nombre = entry_nombre.get().strip()
    corte = combo_corte.get().strip()
    fecha = pd.Timestamp.today()

    if not nombre or not corte:
        messagebox.showwarning("Error", "Ingresa nombre y tipo de corte")
        return

    global database
    nueva_fila = {"Nombre": nombre, "Corte": corte, "Fecha": fecha.date()}
    database = pd.concat([database, pd.DataFrame([nueva_fila])], ignore_index=True)
    database.to_csv(csv_file, index=False)

    messagebox.showinfo("Guardado", f"Cliente {nombre} registrado")
    entry_nombre.delete(0, tk.END)
    combo_corte.set("")


# Botón guardar
tk.Button(root, text="Guardar", command=guardar).pack(pady=10)

#Botón registro de cliente 

registrar_cliente = tk.Button(root, text= "Registrar nuevo cliente", command= registro).pack(pady= 10)



root.mainloop()