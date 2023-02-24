import gui
import sys
import menu

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "menu":
            menu.iniciar()
        else:
            print("Opción no válida")
    else:
        app = gui.Ventana_principal()
        app.mainloop()