from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, showwarning

class Casillas_Rellenar:

    def build(self):
        
        self.nombre = Label(self, text = "Nombre: ")
        self.nombre.config(font=("Arial", 12, "bold"))
        self.nombre.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.mi_nombre = StringVar()
        self.caja_nombre = Entry(self, textvariable = self.mi_nombre)
        self.caja_nombre.config(font=("Arial", 12))
        self.caja_nombre.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.apellido = Label(self, text = "Apellido: ")
        self.apellido.config(font=("Arial", 12, "bold"))
        self.apellido.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.mi_apellido = StringVar()
        self.caja_apellido = Entry(self, textvariable = self.mi_apellido)
        self.caja_apellido.config(font=("Arial", 12))
        self.caja_apellido.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.dni = Label(self, text = "DNI: ")
        self.dni.config(font=("Arial", 12, "bold"))
        self.dni.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.mi_dni = StringVar()
        self.caja_dni = Entry(self, textvariable = self.mi_dni)
        self.caja_dni.config(font=("Arial", 12))
        self.caja_dni.grid(row = 2, column = 1, padx = 10, pady = 10)
        

        self.boton_guardar = Button(self, text = "Guardar", command = self.guardar)
        self.boton_guardar.config(width = 20, font=("Arial", 12, "bold"),
                                bg = "green", fg = "white", cursor = "hand2",
                                activebackground= "#35BD6F")
        self.boton_guardar.configure(state = NORMAL)
        self.boton_guardar.grid(row = 3, column = 0, padx = 10, pady = 10)

        self.boton_cancelar = Button(self, text = "Cancelar", command = self.destroy)
        self.boton_cancelar.config(width = 20, font=("Arial", 12, "bold"),
                                bg = "red", fg = "white", cursor = "hand2",
                                activebackground= "#35BD6F")
        self.boton_cancelar.configure(state = NORMAL)
        self.boton_cancelar.grid(row = 3, column = 1, padx = 10, pady = 10)

        

class Ventana_principal(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de clientes (Ventana principal)")
        self.geometry("900x300")
        self.resizable(1, 1)
        self.config(bg="light blue")
        self.build()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview["columns"] = ("Id", "Nombre", "Apellido", "Dni")

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("Id", anchor=CENTER)
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("Apellido", anchor=CENTER)
        treeview.column("Dni", anchor=CENTER)

        treeview.heading("Id", text="Id", anchor=CENTER)
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Apellido", text="Apellido", anchor=CENTER)
        treeview.heading("Dni", text="Dni", anchor=CENTER)

        scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=treeview.yview)
        treeview.configure(yscroll=scrollbar.set)

        treeview.pack()

        frame = Frame(self)
        frame.pack(padx = 20, pady = 20)

        Button(frame, text="Crear", command=self.create).grid(row = 0, column = 0)
        Button(frame, text="Editar", command=self.edit).grid(row = 0, column = 1)
        Button(frame, text="Eliminar", command=self.delete).grid(row = 0, column = 2)

        self.treeview = treeview


    def create(self):
        Ventana_crear_cliente(self)

    def edit(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, "values")
            Ventana_editar_cliente(self, campos)
        else:
            showwarning("Editar cliente", "Debe seleccionar un cliente")

    def delete(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, "values")
            if askokcancel("Eliminar cliente", 
                           f"¿Está seguro que desea eliminar al cliente {campos[1]} {campos[2]}?"):
                self.treeview.delete(cliente)
        else:
            showwarning("Eliminar cliente", "Debe seleccionar un cliente")


class Ventana_crear_cliente(Toplevel, Casillas_Rellenar):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestor de clientes (Crear cliente)")
        self.geometry("500x300")
        self.resizable(1, 1)
        self.config(bg="light green")
        self.build()

    def guardar(self):
        pass

class Ventana_editar_cliente(Toplevel, Casillas_Rellenar):
    def __init__(self, parent, cliente):
        super().__init__(parent)
        self.title("Gestor de clientes (Editar cliente)")
        self.geometry("500x300")
        self.resizable(1, 1)
        self.config(bg="light green")
        self.build()

    def guardar(self):
        pass


if __name__ == "__main__":
    app = Ventana_principal()
    app.mainloop()