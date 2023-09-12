import re

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
            return print(f"¡Bienvenidos al inicio de nuestro emocionante curso, {self.tituloCurso}!\n Descubre una experiencia educativa única sobre {self.descripcion}\n el objetivo es {self.objetivo}.\n Explora nuestro completo Programa: {self.programa}\n diseñado para tu éxito. ¡Inscríbete hoy mismo  el valor es ${self.costo}\n Duracion de  {self.duracionMeses}\n de aprendizaje para gente de un nivel {self.categoria}!")
        else:
            return print("El curso actualmente no esta disponible ")
        
        
    def nivelCurso(self):  #Mostrar dificultad del curso
         print(f"El curso de {self.tituloCurso} tiene un nivel {self.categoria}")
        



"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

class Clase:
    def __init__(self, fechaClase, tituloClase, contenidoClase, driveClase ):
        self.fechaClase = fechaClase
        self.tituloClase = tituloClase
        self.contenidoClase = contenidoClase
        self.driveClase = driveClase

    def  visualisarClase(self): #Info de la clase
                 print (f"\n titulo: {self.tituloClase}\n\n Fecha de la clase: {self.fechaClase} \n\n Contenido de la clase: {self.contenidoClase} \n\n URLDrive: {self.driveClase} ")
    

    def linkDrive(self): #Link del drive
         return print(f"{self.tituloClase}\n Drive: {self.driveClase}")
                 

"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

class Usuario:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado,  rol):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.estado = estado
        self.rol =  rol


    def datosInteresados(self): #Info del usuario interesado
         return print(f" nombre: {self.nombre} \n Apellido: {self.apellido} \n dni: {self.dni} \n direccion {self.direccion} \n fecha: {self.fechaNacimiento} \n localidad: {self.localidad} \n  codigo postal: {self.codigo}, \n provincia: {self.provincia},\n telefono: {self.telefono},\n Email: {self.email}")


    def validacionEmail(self):       #Validar el Email y activacion de la cuenta
         patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
         if  re.match(patron, self.email):
            print(f"Se envio un codigo de validacion a su correo: {self.email}")

            while True:
                codigo1 = input("ingresa el el codigo recibido: ")
                print()
                codigo2 = input("repite nuevamente el codigo: ")
                if codigo1 == codigo2 and codigo1 != "":
                      self.estado = "Activo"
                      print(f"El codigo fue correcto Bienvenido {self.nombre}")
                      print()
                      break
                else:
                      print ("el codigo no es correcto vuelve a intentarlo")
                      print()
            
         else:
            print("Correo no valido ")



"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""


class Docentes(Usuario):         
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado, rol):
         super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado, rol)


    def  datosDocentes(self):     #Datos de los docentes
        if self.rol ==  "Profesor":
         return print(f" Nombre: {self.nombre} \n apllido: {self.apellido}\n Dni: {self.dni} \n Celular: {self.telefono_celular} \n Email: {self.email} \n Rol: {self.rol}")
        else:
             print("El usuario no es Profesor")


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

class Administrador():
                
    def __init__(self, usuario, telefono_celular, email, estado, rol, clave_acceso):
        self.usuario = usuario
        self.telefono_celular =  telefono_celular
        self.email = email
        self.estado = estado
        self.rol =  rol
        self.clave_acceso = clave_acceso



    def deshabilitar_cuenta(self, usuario): 
        usuarioAdmin = input("Ingresa el Usuario Administrador: ")
        contraseñaAdmin = input("Ingresa la contraseña: ")

        if  usuarioAdmin == self.usuario and contraseñaAdmin == self.clave_acceso:
            usuario.estado = "Inactivo"

            print(f"Cuenta de {usuario.nombre} deshabilitada.")
        else:
            print ("las credenciales son incorrectas.")


    def habilitar_Cuenta(self, usuario):
        usuarioAdmin = input("Ingresa el Usuario Administrador: ")
        contraseñaAdmin = input("Ingresa la contraseña: ")

        if  usuarioAdmin == self.usuario and contraseñaAdmin == self.clave_acceso:
          usuario.estado = "Activo"

          print ( f"{usuario.nombre}'s Cuenta ha sido activada." )
          
        else:
            print ("las credenciales son incorrectas.")

        
    def asignar_Rol(self, usuario):     #Asignarle el rol al usuario Profesor/Alumno/Administrador
        usuarioAdmin = input("Ingresa el Usuario Administrador: ")
        contraseñaAdmin = input("Ingresa la contraseña: ")

        if  usuarioAdmin == self.usuario and contraseñaAdmin == self.clave_acceso:
         if self.rol == "Administrador":
              print(f"-----!Que Rol Desea asignarlse ah {usuario.nombre}!-----")
              print("")
              print("-----------------| 1 |  Profesor |-----------------")
              print("")
              print("-----------------| 2 |  Alumno |-----------------")
              print()
              print("-----------------| 3 |  Administrador |-----------------")

         numero = int(input("Ingrese El numero: "))
         
         if numero == 1:
            usuario.rol = "Profesor"
            print(f"{usuario.nombre} Tiene rango Profesor")
            print()
            print("---------------------------------------------------------------------------")
         elif numero == 2:
            usuario.rol = "Alumno"
            print(f"{usuario.nombre} Tiene rango Alumno")
            print()
            print("---------------------------------------------------------------------------")
         elif numero == 3:
            usuario.rol = "Administrador"
            print(f"{usuario.nombre} Tiene rango Administrador")
            print()
            print("---------------------------------------------------------------------------")
         else:
               print('No existe ese número')
        else:
                         print ('Usuario no encontrado.')


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""


class UsuarioFinal(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado, rol):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado, rol)
        self.curso_inscriptos = []
        self.estado = estado
        self.carrito_compras = None

    def bienvenida(self):  #Bienvenida al usuario
          if self.estado == "Activo":
               return  print(f"Bienvenido {self.nombre}")
          else:
               print (f'Usuario Inactivo')

    def agregar_al_carrito(self, curso): #Agregar al carrito un curso
        if self.carrito_compras is None:
            self.carrito_compras = CarritoCompras()
            self.carrito_compras.agregar_curso(curso)
               


    def seleccionar_medio_pago(self, medio_pago):           #Cargar medio de pago del usuario
        print(f"Usted elijio este medio de pago: {medio_pago.medioDePago}")
        self.medio_pago = medio_pago
     
    def confirmar_compra(self): #Confirmar la compra
        if self.estado and self.medio_pago:
            monto_total = self.carrito_compras.calcular_total()
            print(f"Compra confirmada por {self.nombre} {self.apellido}. Monto total: ${monto_total}")
        else:
            print("No se puede confirmar la compra. Verifique que su cuenta esté activada y que haya seleccionado un medio de pago.")


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

class CarritoCompras:   #Carrito de compra
    def __init__(self,):
        self.cursos = []
        self.medio_pago = None

    def agregar_curso(self, curso):  #Solicitar al usuario cargar el Curso que quiere aregar al carrito
        self.cursos.append(curso)
        print(f"usted agrego al carrito el curso: {curso.tituloCurso}")
        

    def calcular_total(self):    #total del carrito
        total = sum(curso.costo for curso in self.cursos)
        return total
    
    def cuponDescuento(self): #Cupon de descuento
         cupon = "Descuento50%"
         usuario = input("Escribe el cupon de descuento: ")
         if usuario == cupon:
            total = sum(curso.costo for curso in self.cursos)
            return print("Felicidades su cupon es valido El valor final es: ", total * 0.5 )
         
    def seleccionar_medio_pago(self, medio_pago):       #Cargar el medio de pago
        print(f"Usted Cargo estos datos {medio_pago}")
        self.medio_pago = medio_pago
         


class MedioPago:            #Clase de medio de pago para cargar el medio de pago y datos de la tarjeta
    def __init__(self, medioDePago, datos):
        self.medioDePago = medioDePago
        self.datos = datos



"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

class Compra:
    def __init__(self, id_compra, id_carrito_compra, id_medios_pago, id_usuario, fecha,monto_total):
        self.id_compra = id_compra
        self.id_carrito_compra = id_carrito_compra
        self.id_medios_pago = id_medios_pago
        self.id_usuario=id_usuario
        self.fecha = fecha
        self.monto_total = monto_total

"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

class MediosDeContacto(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado, rol, id_medioContacto, fecha):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado, rol)
        self.id_medioContacto = id_medioContacto
        self.fecha = fecha


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

class MedioDeContacto(MediosDeContacto):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado, rol, id_medioContacto, fecha, tipo):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado, rol, id_medioContacto, fecha)
        self.tipo  = tipo

    def mostrarMedioDeContacto(self):
        return print(f"El tipo de medio de contacto Elegido por {self.nombre} {self.apellido} es: {self.tipo}")

"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""




"""----------------------------------------------------Class Cursos----------------------------------------------------------------------------------------"""

curso1 = Cursos("23/03/2024","Administración de Redes Empresariale","habilidades necesarias para gestionar eficientemente redes empresariales, desde configuración hasta seguridad. Aprende a optimizar el rendimiento y garantizar la confiabilidad de la infraestructura de red.", "convertirse en un administrador de redes altamente competente para empresas", "Topologías de red, protocolos, seguridad de redes, administración de switches y routers, monitoreo de red, y más.", 5000, "3 meses","https://alphaenginyeria.com/wp-content/uploads/2022/08/Tipos-de-redes.webp", "Disponible","inicial" )

curso2 = Cursos("8/05/2024","Desarrollo Web Full Stack","Conviértete en un desarrollador web completo. Aprende a crear aplicaciones web desde cero, dominando tanto el frontend como el backend.","Ser un desarrollador web full stack altamente competente", "HTML, CSS, JavaScript, Node.js, React, bases de datos, seguridad, despliegue, y más.",50000,"6 meses", "https://www.freelancermap.com/blog/wp-content/uploads/2020/07/desarrollador-full-stack-resumen-perfil-profesional-funciones-habilidades-formacion-salario.png","Disponible","intermedio")

# curso1.presentacion()  #visualizar la presentacion del curso
# print()
# curso2.presentacion()
# print()
# curso1.nivelCurso()  #ver el nivel de dificultad del curso
# print()
# curso2.nivelCurso()


"""----------------------------------------------------Class Clase----------------------------------------------------------------------------------------"""


redesEmpresariale = Clase("23/03/2023",": Introducción a Redes Empresariales y Conceptos Básicos de Redes","¿Qué son las redes empresariales? importancia de las redes en el entorno empresarial Roles y responsabilidades de un administrador de redes empresariales","https://www.google.com/intl/es-419_ar/drive/")


desarrolladorFullStack = Clase("8/05/2024",  "Introducción al Desarrollo Web y Fundamentos de HTML","¿Qué es HTML? Estructura básica de un documento HTML  Etiquetas, elementos y atributos en HTML Creación de tu primera página HTML","https://www.google.com/intl/es-419_ar/drive/")

# # print()
# redesEmpresariale.visualisarClase()         # ver informacion de la clase de redes
# # print()
# redesEmpresariale.linkDrive()               #ver el link del drive


# desarrolladorFullStack.visualisarClase()  # ver informacion de la clase de desarrollo

# desarrolladorFullStack.linkDrive()



"""----------------------------------------------------Class Usuario----------------------------------------------------------------------------------------"""



usuario = Usuario("Franco","Ferreyra","456789456","23/12/2000","asaf 456","Arroyito","2434","Cordoba","546587465","Franco@gmail.com","Activo","Alumno")

# usuario.datosInteresados()  #Visualizar los datos del usuario

# usuario.validacionEmail()  #Validar si el correo es valido



"""----------------------------------------------------Class Docente----------------------------------------------------------------------------------------"""


docente1  = Docentes("Carina","Scaglia","4567893","26/09/1966","Alfonsin storni 111","el Tio","2432","Cordoba","3215498","Scaglia@gmail.com","Activo","Profesor")
docente2  = Docentes("roberto","migotti","35654641","11/04/1968"," storni 1111","Arroyito","2434","Cordoba","357689897","roberto@gmail.com","Activo","Profesor")
          
# docente1.datosDocentes() #ver los datos del docente
# print()
# docente2.datosDocentes()


# UsuarioX = Docentes("pablo","belmonte","5464","26/08/1975","CalleFalsa 123","Arroyito","2434","Cordoba","3546789","Pablo@gmail.com","Activo","Alumno")
# UsuarioX.datosDocentes() # No te deja entrar por que no tiene rango Profesor
# usuarioAdministrador.asignar_Rol(UsuarioX)  # Le asigno rango profesor
# UsuarioX.datosDocentes() #Te deja ingresar y ver los datos



"""----------------------------------------------------Class UsuarioFinal----------------------------------------------------------------------------------------"""

usuarioN1 = UsuarioFinal("Santiago","Ferreyra","43884795","35/03/2900","Calle falsa 123","Arroyito","2434","Cordoba","3576464646","Santiago@gmail.com","Activo","Alumno")

# usuarioN1.bienvenida()

# usuarioN1.bienvenida()


# usuarioFinal.validacionEmail()


"""----------------------------------------------------Class Administrador ----------------------------------------------------------------------------------------"""

usuarioAdministrador = Administrador("Admin","123456798","Administrador@gmail.com","Activo","Administrador","Admin$158")


# usuarioAdministrador.deshabilitar_cuenta(usuarioN1)
# usuarioAdministrador.asignar_Rol(usuarioN1)


# usuarioFinal2 = UsuarioFinal("vico","sosa","6544654","avellaneda  452","11/11/1990","juansosa@gmail.com","3215648","hola123","Alumno", "Inactivo")

# usuarioAdministrador.deshabilitar_cuenta(usuarioFinal2)  #Desastivar cuenta de usuario
# usuarioFinal2.bienvenida() # No te da  la bienvenida por que esta inactiva
# usuarioAdministrador.habilitar_Cuenta(usuarioFinal2) #Activar Cuenta
# usuarioFinal2.bienvenida() # te da la bienvenida por que esta la cuenta activa 


# UsuarioX = Docentes("pablo","belmonte","5464","26/08/1975","CalleFalsa 123","Arroyito","2434","Cordoba","3546789","Pablo@gmail.com","Activo","Alumno")
# UsuarioX.datosDocentes() # No te deja entrar por que no tiene rango Profesor
# usuarioAdministrador.asignar_Rol(UsuarioX)  # Le asigno rango profesor
# UsuarioX.datosDocentes() #Te deja ingresar y ver los datos


"""----------------------------------------------------Class  CarritoCompras----------------------------------------------------------------------------------------"""

carritoCompras = CarritoCompras()
# carritoCompras.agregar_curso(curso1) #Agregar curso al carrito
# print("El valor total es:", carritoCompras.calcular_total())   #Da valor de 5000
# carritoCompras.cuponDescuento() #Cupon de descuento Codigo: Descuento50% queda en 2500


"""----------------------------------------------------Class  CarritoCompras----------------------------------------------------------------------------------------"""

usuarioN1 = UsuarioFinal("Santiago","Ferreyra","43884795","35/03/2900","Calle falsa 123","Arroyito","2434","Cordoba","3576464646","Santiago@gmail.com","Activo","Alumno")


# usuarioFinal.agregar_al_carrito(curso1) #Agregar el carrito
# medio_pago = MedioPago("Tarjeta de Crédito Mercado Pago", "Número de tarjeta: 5644-56654-89654-56489")  #llamo ala clase que carga los datos de la tarjeta
# usuarioFinal.seleccionar_medio_pago(medio_pago) #llamo al metodo para seleccionar los medios de pago

# usuarioFinal.confirmar_compra()  # Confirmo la compra

# usuarioFinal.inscripcionCurso(curso1.tituloCurso)

# usuarioFinal.inscripcionCurso(curso1.tituloCurso) #Forzar el else



"""----------------------------------------------------Class  MedioDeContactos----------------------------------------------------------------------------------------"""

usuarioContacto1 = MedioDeContacto("Pedro","Perez","4654321","16/01/1966","Calle falsa 123","El tio","2434","Cordoba","32478341","pedro@gmail.com","Activo","Alumno","222","18/03/2023","Whatssap")
usuarioContacto2 = MedioDeContacto("franco","Ferreyra","4654321","28/06/1975","Calle falsa 123","arroyito","2434","Cordoba","324465341","gato@gmail.com","Activo","Alumno","223","16/08/2023","Referido interno")
usuarioContacto3 = MedioDeContacto("carolina","carignano","4654321","14/08/1986","Calle falsa 123","El tio","2434","Cordoba","32478341","pedro@gmail.com","Activo","Alumno","224","22/01/2023","Call Center")
usuarioContacto4 = MedioDeContacto("antonio","pascal","444654321","22/06/1995","Calle falsa 123","arroyito","2434","Cordoba","32478341","antinop@gmail.com","Activo","Alumno","225","25/06/2023","Correo Electronico")


# usuarioContacto1.mostrarMedioDeContacto()
# usuarioContacto2.mostrarMedioDeContacto()
# usuarioContacto3.mostrarMedioDeContacto()
# usuarioContacto4.mostrarMedioDeContacto()