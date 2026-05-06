class Libro(object):
    _next_id = 0

    def __init__(self, titulo):
        self.titulo = titulo
        self.id = Libro._next_id
        self.autor = None
        self.editorial = None 
        Libro._next_id = Libro._next_id + 1
    
    def asignar_autor(self, autor):
        self.autor = autor

    def asignar_editorial(self, editorial):
        self.editorial = editorial

    def __str__(self):
        return f"ID: {self.id}, Titulo: {self.titulo}, Autor: {self.autor.nombre} "


if __name__ == "__main__":
    from persona import Autor
    import os
    libro = Libro("Programacion sin sentido")
    libro.asignar_editorial("Kapeluz")
    emiliano = Autor("Emiliano", 29250006)
    emiliano.agregrar_biografia("Emiliano es autor de muchos libros que nadie entiende y nadie junca leyó")
    libro.asignar_autor(emiliano)


    lista_libros = [libro]
    finalizar = False
    while not finalizar:

        print("=== Menú BIBLIOTECA DSOO ===\nOpciones:\n\t1.) Cargar un libro\n\t2.) Listar libros\n\t3.) Salir del sistema")
        opcion = int(input("Ingrese una opcion: "))


        if opcion == 2:
            for i in lista_libros:
                print(i)
        elif opcion == 3:
            finalizar = True
        elif opcion == 1:
            print("Funcionalidad no implementada")

        input("\n\n -- Ingrese una tecla par continuar --")
        os.system("clear")