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
            return print(f"¡Bienvenidos al inicio de nuestro emocionante curso, {self.tituloCurso}!\n Descubre una experiencia educativa única sobre {self.descripcion}\n el objetivo es {self.objetivo}.\n Explora nuestro completo Programa: {self.programa}\n diseñado para tu éxito. ¡Inscríbete hoy mismo  el valor es ${self.costo}\n Duracion de  {self.duracionMeses}\n de aprendizaje para gente de un nivel {self.categoria}!")
        else:
            return print("El curso actualmente no esta disponible ")
        
        
    def nivelCurso(self):  #Mostrar dificultad del curso
         print(f"El curso de {self.tituloCurso} tiene un nivel {self.categoria}")
        
        
        
curso1 = Cursos("23/03/2024","Administración de Redes Empresariale","habilidades necesarias para gestionar eficientemente redes empresariales, desde configuración hasta seguridad. Aprende a optimizar el rendimiento y garantizar la confiabilidad de la infraestructura de red.", "convertirse en un administrador de redes altamente competente para empresas", "Topologías de red, protocolos, seguridad de redes, administración de switches y routers, monitoreo de red, y más.", 5000, "3 meses","https://alphaenginyeria.com/wp-content/uploads/2022/08/Tipos-de-redes.webp", "Disponible","inicial" )

curso2 = Cursos("8/05/2024","Desarrollo Web Full Stack","Conviértete en un desarrollador web completo. Aprende a crear aplicaciones web desde cero, dominando tanto el frontend como el backend.","Ser un desarrollador web full stack altamente competente", "HTML, CSS, JavaScript, Node.js, React, bases de datos, seguridad, despliegue, y más.",50000,"6 meses", "https://www.freelancermap.com/blog/wp-content/uploads/2020/07/desarrollador-full-stack-resumen-perfil-profesional-funciones-habilidades-formacion-salario.png","Disponible","intermedio")



# curso1.presentacion()  #visualizar la presentacion del curso
# print()
# curso2.presentacion()
# print()
# curso1.nivelCurso()  #ver el nivel de dificultad del curso
# print()
# curso2.nivelCurso()




"""Por otro lado, los cursos contienen un
conjunto de clases, en donde por cada clase se debe mostrar la fecha, título, contenido,
URLDrive."""

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
                 


redesEmpresariale = Clase("23/03/2023",": Introducción a Redes Empresariales y Conceptos Básicos de Redes","¿Qué son las redes empresariales? importancia de las redes en el entorno empresarial Roles y responsabilidades de un administrador de redes empresariales","https://www.google.com/intl/es-419_ar/drive/")


desarrolladorFullStack = Clase("8/05/2024",  "Introducción al Desarrollo Web y Fundamentos de HTML","¿Qué es HTML? Estructura básica de un documento HTML  Etiquetas, elementos y atributos en HTML Creación de tu primera página HTML","https://www.google.com/intl/es-419_ar/drive/")

# # print()
# redesEmpresariale.visualisarClase()         # ver informacion de la clase de redes
# # print()
# redesEmpresariale.linkDrive()               #ver el link del drive


# desarrolladorFullStack.visualisarClase()  # ver informacion de la clase de desarrollo

# desarrolladorFullStack.linkDrive()

"""
clase de un curso la dicta un docente, y este puede participar en el dictado de varias
clases y de varios cursos. De cada docente se desea guardar su apellido, nombre, dni, fecha
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email"""


class Docentes:         #Clase docentes
    def __init__(self,nombre, apellido, dni, fechaNacimiento, direccion, localidad, codigoPostal, provincia, celular, email, estado, rol ):
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
        self.estado = estado
        self.rol = rol

          
    def  datosDocentes(self):     #Datos de los docentes
        if self.rol ==  "Profesor":
         return print(f" Nombre: {self.nombre} \n apllido: {self.apellido}\n Dni: {self.dni} \n Celular: {self.celular} \n Email: {self.email} \n Rol: {self.rol}")
        else:
             print("El usuario no es Profesor")

docente1  = Docentes("Carina","Scaglia","3589541","18/09/1978","Alfonsin storni 1111","Arroyito","2434","Cordoba","3576464646","cari@gmail.com","Activo","Profesor")
docente2  = Docentes("roberto","migotti","35654641","11/04/1968"," storni 1111","Arroyito","2434","Cordoba","357689897","roberto@gmail.com","Activo","Profesor")
          
# docente1.datosDocentes() #ver los datos del docente
# print()
# docente2.datosDocentes()


"""Por otra parte, los interesados en inscribirse a un curso deberán crearse una cuenta de usuario
final, donde deberán registrar su datos personales (nombre, apellido, dni, dirección, fecha
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email), además de
confirmar y reconfirmar una clave de acceso. Para la activación de la cuenta de usuario final se
deberá validar que el email sea verdadero y esté en funcionamiento, enviando un correo
 automático al email registrado."""


class interesados:    #Datos de interesados
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

    def datosInteresados(self): #Info del usuario interesado
         return print(f" nombre: {self.nombre} \n Apellido: {self.apellido} \n dni: {self.dni} \n direccion {self.direccion} \n fecha: {self.fechaNacimiento} \n localidad: {self.localidad} \n  codigo postal: {self.codigo}, \n provincia: {self.provincia},\n telefono: {self.telefono},\n Email: {self.email}")


    def validacionEmail(self):       #Validar el Email y activacion de la cuenta
         patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
         if  re.match(patron, self.email):
            print(f"Se envio un codigo de validacion a su correo: {self.email}")

            while True:
                codigo1 = input("ingresa el el codigo recibido: ")
                print()
                codigo2 = input("repide nuevamente el codigo: ")
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


    

usuario = interesados("Santiago","Ferreyra","43888888","callefalsa123","23/03/2002","arroyito","2434","Cordoba","35764646466","hasdg@gmail.com")

# usuario.datosInteresados()  #Visualizar los datos del usuario

# usuario.validacionEmail()  #Validar si el correo es valido




"""Por último, los usuarios finales podrán agregar uno o más cursos en un carrito de compras,
donde se deberá visualizar: Foto, título del curso, duración, costo. Una vez confirmados los
ítems del carrito, deberá seleccionar el medio de pago, los cuales pueden ser: Tarjeta de
crédito/débito y transferencia bancaria; a fin de tener más datos acerca de los medios de
pago, deberán registrarse los datos básicos de tarjetas y transferencias). Al confirmar la
compra, se deberá registrar además la fecha de compra, el usuario que realiza la compra y el
monto total. Dada la consigna anterior, se pide: identificar, analizar y documentar los
requisitos según el formato de historias de usuario. Para la creación de las historias, hacer uso
del repositorio Github, a través de creación de issues."""




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
         

    
carritoCompras = CarritoCompras()
# carritoCompras.agregar_curso(curso1) #Agregar curso al carrito
# print("El valor total es:", carritoCompras.calcular_total())   #Da valor de 5000
# carritoCompras.cuponDescuento() #Cupon de descuento Codigo: Descuento50% queda en 2500

class MedioPago:            #Clase de medio de pago para cargar el medio de pago y datos de la tarjeta
    def __init__(self, medioDePago, datos):
        self.medioDePago = medioDePago
        self.datos = datos



"""Los usuarios públicos registrados pueden inscribirse a uno o más cursos. Además, el sitio
deberá proveer la posibilidad de registrar 2 roles más de usuarios quienes también tendrán
interacción con el sistema: Administrador, Docente. Los usuarios también deben tener
asociado un estado (Activo / Inactivo)."""


class UsuarioFinal:  
     def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, email, telefono, clave_acceso, rol, estado):
          self.nombre = nombre
          self.apellido = apellido
          self.dni = dni
          self.direccion = direccion
          self.fecha_nacimiento = fecha_nacimiento
          self.email = email
          self.telefono = telefono
          self.clave_acceso = clave_acceso
          self.rol = rol
          self.curso_inscriptos = []
          self.estado = estado
          self.carrito_compras = None


     def inscripcionCurso(self, curso):  #Inscribirse a un curso viendo si no esta inscripto ya en ese curso
               if curso not in  self.curso_inscriptos and self.estado == "Activo":
                    self.curso_inscriptos.append(curso)
                    print(f"{self.nombre} se ha inscrito en el curso {curso}.")
               else:
                 print(f"{self.nombre} ya está inscrito en el curso {curso}.")


     def validacionEmail(self):
         patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
         if  re.match(patron, self.email):
            print(f"Se envio un codigo de validacion a su correo: {self.email}")

            while True:
                codigo1 = input("ingresa el el codigo recibido: ")
                print()
                codigo2 = input("repide nuevamente el codigo: ")
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


usuarioFinal = UsuarioFinal("juan","sosa","6544654","avellaneda  452","11/11/1990","juansosa@gmail.com","3215648","hola123","usuario", "Activo")

# usuarioFinal.agregar_al_carrito(curso1) #Agregar el carrito
# medio_pago = MedioPago("Tarjeta de Crédito Mercado Pago", "Número de tarjeta: 5644-56654-89654-56489")  #llamo ala clase que carga los datos de la tarjeta
# usuarioFinal.seleccionar_medio_pago(medio_pago) #llamo al metodo para seleccionar los medios de pago

# usuarioFinal.confirmar_compra()  # Confirmo la compra

# usuarioFinal.inscripcionCurso(curso1.tituloCurso)

# usuarioFinal.validacionEmail()

# usuarioFinal.inscripcionCurso(curso1.tituloCurso) #Forzar el else





class Administrador:
     nombre = ""
     def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, email, telefono, clave_acceso, estado,  rol):
          self.nombre = nombre
          self.apellido = apellido
          self.dni = dni
          self.direccion = direccion
          self.fecha_nacimiento = fecha_nacimiento
          self.email = email
          self.telefono = telefono
          self.clave_acceso = clave_acceso
          self.estado = estado
          self.rol = rol



     def deshabilitar_cuenta(self, usuario): 
        usuario.estado = "Inactivo"
        print(f"Cuenta de {usuario.nombre} deshabilitada.")


     def habilitar_Cuenta(self, usuario):
          usuario.estado = "Activo"
          print(f"Cuenta de {usuario.nombre} Se encuentra Activa")

        
     def asignar_Rol(self, usuario):     #Asignarle el rol al usuario Profesor/Alumno/Administrador
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



usuarioAdministrador = Administrador("admin","admin","456465","asdgasd 123", "23/03/2002","admin@gmail.com","2316546", "SoyAdmin123", "Activo", "Administrador")






usuarioFinal2 = UsuarioFinal("vico","sosa","6544654","avellaneda  452","11/11/1990","juansosa@gmail.com","3215648","hola123","Alumno", "Inactivo")

# usuarioAdministrador.deshabilitar_cuenta(usuarioFinal2)  #Desastivar cuenta de usuario
# usuarioFinal2.bienvenida() # No te da  la bienvenida por que esta inactiva
# usuarioAdministrador.habilitar_Cuenta(usuarioFinal2) #Activar Cuenta
# usuarioFinal2.bienvenida() # te da la bienvenida por que esta la cuenta activa 



# UsuarioX = Docentes("pablo","belmonte","5464","26/08/1975","CalleFalsa 123","Arroyito","2434","Cordoba","3546789","Pablo@gmail.com","Activo","Alumno")
# UsuarioX.datosDocentes() # No te deja entrar por que no tiene rango Profesor
# usuarioAdministrador.asignar_Rol(UsuarioX)  # Le asigno rango profesor
# UsuarioX.datosDocentes() #Te deja ingresar y ver los datos
