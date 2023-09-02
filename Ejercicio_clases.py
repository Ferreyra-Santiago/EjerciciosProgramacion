import re #Validar email

# Crear todas las clases que fueran necesarias para iniciar un proceso de desarrollo de
# software de la siguiente situación:
# Una empresa privada que se dedica a la venta de cursos de oficios, desea desarrollar un
# sistema web para poder publicar su oferta académica. Dicho sistema debe mostrar una serie
# de cursos disponibles.


"""
Por cada curso se deberá visualizar la fecha de comienzo, título, descripción, objetivos,
programa, costo, duración en meses, foto y estado (disponible o no disponible, en base a su
estado deberán verse o no en el sitio). A su vez, cada curso pertenece a alguna de las
siguientes categorías (Inicial, Intermedio, Avanzado). Por otro lado, los cursos contienen un
conjunto de clases, en donde por cada clase se debe mostrar la fecha, título, contenido,
URLDrive."""

class Cursos:
    def __init__(self,inicio, tituloCurso, descripcion, objetivo, programa, costo, duracionMeses, fotos, estado, categoria ):
        self.inicio = inicio
        self.tituloCurso = tituloCurso
        self.descripcion = descripcion
        self.objetivo = objetivo
        self.programa = programa
        self.costo = costo
        self.duracionMeses = duracionMeses
        self.fotos = fotos
        self.estado = estado
        self.categoria = categoria

    def presentacion(self):  #Clase para presentar el curso
        if self.estado == "Disponible":
            return print(f"¡Bienvenidos al inicio de nuestro emocionante curso, {self.tituloCurso}!\n Descubre una experiencia educativa única sobre {self.descripcion}\n el objetivo es {self.objetivo}.\n Explora nuestro completo Programa: {self.programa}\n diseñado para tu éxito. ¡Inscríbete hoy mismo  el valor es {self.costo}\n Duracion de  {self.duracionMeses}\n de aprendizaje para gente de un nivel {self.categoria}!")
        else:
            return print("El curso actualmente no esta disponible ")
        
        
    def nivelCurso(self):
         print(f"El curso de {self.tituloCurso} tiene un nivel {self.categoria}")
        
        
        
curso1 = Cursos("23/03/2024","Administración de Redes Empresariale","habilidades necesarias para gestionar eficientemente redes empresariales, desde configuración hasta seguridad. Aprende a optimizar el rendimiento y garantizar la confiabilidad de la infraestructura de red.", "convertirse en un administrador de redes altamente competente para empresas", "Topologías de red, protocolos, seguridad de redes, administración de switches y routers, monitoreo de red, y más.", "$5000", "3 meses","https://alphaenginyeria.com/wp-content/uploads/2022/08/Tipos-de-redes.webp", "Disponible","inicial" )

curso2 = Cursos("8/05/2024","Desarrollo Web Full Stack","Conviértete en un desarrollador web completo. Aprende a crear aplicaciones web desde cero, dominando tanto el frontend como el backend.","Ser un desarrollador web full stack altamente competente", "HTML, CSS, JavaScript, Node.js, React, bases de datos, seguridad, despliegue, y más.","$50.000","6 meses", "https://www.freelancermap.com/blog/wp-content/uploads/2020/07/desarrollador-full-stack-resumen-perfil-profesional-funciones-habilidades-formacion-salario.png","Disponible","intermedio")



curso1.presentacion()  #visualizar la presentacion del curso
print()
curso2.presentacion()
print()
curso1.nivelCurso()  #ver el nivel de dificultad del curso
print()
curso2.nivelCurso()




"""Por otro lado, los cursos contienen un
conjunto de clases, en donde por cada clase se debe mostrar la fecha, título, contenido,
URLDrive."""

class Clase:
    def __init__(self, fechaClase, tituloClase, contenidoClase, driveClase ):
        self.fechaClase = fechaClase
        self.tituloClase = tituloClase
        self.contenidoClase = contenidoClase
        self.driveClase = driveClase

    def  visualisarClase(self):
                 print (f"\n titulo: {self.tituloClase}\n\n Fecha de la clase: {self.fechaClase} \n\n Contenido de la clase: {self.contenidoClase} \n\n URLDrive: {self.driveClase} ")
    

    def linkDrive(self):
         return print(f"{self.tituloClase}\n Drive: {self.driveClase}")
                 


redesEmpresariale = Clase("23/03/2023",": Introducción a Redes Empresariales y Conceptos Básicos de Redes","¿Qué son las redes empresariales? importancia de las redes en el entorno empresarial Roles y responsabilidades de un administrador de redes empresariales","https://www.google.com/intl/es-419_ar/drive/")


desarrolladorFullStack = Clase("8/05/2024",  "Introducción al Desarrollo Web y Fundamentos de HTML","¿Qué es HTML? Estructura básica de un documento HTML  Etiquetas, elementos y atributos en HTML Creación de tu primera página HTML","https://www.google.com/intl/es-419_ar/drive/")

# print()
redesEmpresariale.visualisarClase()         # ver informacion de la clase de redes
# print()
redesEmpresariale.linkDrive()               #ver el link del drive


desarrolladorFullStack.visualisarClase()  # ver informacion de la clase de desarrollo

desarrolladorFullStack.linkDrive()

"""
clase de un curso la dicta un docente, y este puede participar en el dictado de varias
clases y de varios cursos. De cada docente se desea guardar su apellido, nombre, dni, fecha
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email"""


class Docentes:
    def __init__(self,nombre, apellido, dni, fechaNacimiento, direccion, localidad, codigoPostal, provincia, celular, email, ):
        self.nombre = nombre
        self.apellido = apellido
        self.dni =  dni
        self.fechaNacimiento  = fechaNacimiento
        self.direccion = direccion
        self.localidad =  localidad
        self.codigoPostal = codigoPostal
        self.provincia = provincia
        self.celular = celular
        self.email = email
          
    def  datosDocentes(self):
        return print(f" Nombre: {self.nombre} \n apllido: {self.apellido}\n Dni: {self.dni} \n Celular: {self.celular} \n Email: {self.email}")
    
docente1  = Docentes("Carina","Scaglia","3589541","18/09/1978","Alfonsin storni 1111","Arroyito","2434","Cordoba","3576464646","cari@gmail.com")
docente2  = Docentes("roberto","migotti","35654641","11/04/1968"," storni 1111","Arroyito","2434","Cordoba","357689897","roberto@gmail.com")
          
docente1.datosDocentes() #ver los datos del docente
print()
docente2.datosDocentes()


"""Por otra parte, los interesados en inscribirse a un curso deberán crearse una cuenta de usuario
final, donde deberán registrar su datos personales (nombre, apellido, dni, dirección, fecha
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email), además de
confirmar y reconfirmar una clave de acceso. Para la activación de la cuenta de usuario final se
deberá validar que el email sea verdadero y esté en funcionamiento, enviando un correo
 automático al email registrado."""


class interesados:
    def __init__(self,nombre, apellido, dni, dirección, fechaNacimiento, localidad, codigoPostal, provincia, telefono,  email ):
         self.nombre  = nombre
         self.apellido = apellido
         self.dni = dni
         self.direccion = dirección
         self.fechaNacimiento = fechaNacimiento

         self.localidad =  localidad
         self.codigo = codigoPostal
         self.provincia =  provincia
         self.telefono = telefono

         self.email = email

    def datosInteresados(self):
         return print(f" nombre: {self.nombre} \n Apellido: {self.apellido} \n dni: {self.dni} \n direccion {self.direccion} \n fecha: {self.fechaNacimiento} \n localidad: {self.localidad} \n  codigo postal: {self.codigo}, \n provincia: {self.provincia},\n telefono: {self.telefono},\n Email: {self.email}")


    def validacionEmail(self):
         patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
         if  re.match(patron, self.email):
            print("Se envio un codigo de validacion a su correo")
         else:
            print("Correo no valido ")

usuario = interesados("Santiago","Ferreyra","43888888","callefalsa123","23/03/2002","arroyito","2434","Cordoba","35764646466","hasdg@gmail.com")

usuario.datosInteresados()  #Visualizar los datos del usuario

usuario.validacionEmail()  #Validar si el correo es valido





















































"""primera clase menu a terminar"""

# print("--------------------Bienvenido -------------------")
# print()
# print("--------------------| Menu |-------------------")
# print("")
# print("-----!seleccione una opcion para continuar!-----")
# print("")
# print("-----------------| 1 |  Ver Cursos |-----------------")
# print("")
# print("-----------------| 2 |  Ver dificultad del curso |-----------------")
# print("")


# numero = int(input("ingrese numero:  "))
# print()

# if numero == 1:
#         curso1.presentacion()
#         print()
#         print("---------------------------------------------------------------------------")
#         curso2.presentacion()
#         print()
# elif numero == 2:
#         curso1.nivelCurso()
#         print()
#         print("---------------------------------------------------------------------------")
#         print()
#         curso2.nivelCurso()
#         print()
# else:
#      print ("Opcion invalida, vuelva a intentarlo.")










# nombre = input()
# apellido = input()
# dni= int(input)
# direccion = input()
# fechaNacimiento = input()
# localidad =input()
# codigoPostal =input()
# provincia =input()
# telefonoCelular =input()
# email =input()
