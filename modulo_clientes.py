from abc import ABC, abstractmethod
import re

# 1. MANEJO DE EXCEPCIONES PERSONALIZADAS
class ValidacionError(Exception):
    """Excepción base para errores de validación en el sistema."""
    pass

class ClienteError(ValidacionError):
    """Excepción específica para errores de datos de Clientes."""
    pass


# 2. CLASE ABSTRACTA

class Entidad(ABC):
    """Clase abstracta que representa entidades generales del sistema."""
    
    def __init__(self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre

    # protección (encapsulamiento) de datos.
    @property
    @abstractmethod
    def identificacion(self):
        pass

    @property
    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass


# 3. CLASE CLIENTE CON ENCAPSULACIÓN

class Cliente(Entidad):
    """Clase Cliente con validaciones robustas y datos encapsulados."""
    
    def __init__(self, identificacion, nombre, correo, telefono):
        # Los atributos inician privados (__)
        self.__identificacion = None
        self.__nombre = None
        self.__correo = None
        self.__telefono = None

        # Al usar 'self.atributo' sin guiones, activamos los validadores (setters)
        # desde el momento en que se crea el objeto.
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # ENCAPSULACIÓN Y VALIDACIÓN: IDENTIFICACIÓN
    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        # Validación: Solo debe contener números
        if not valor or not str(valor).isdigit():
            raise ClienteError(f"Identificación inválida: '{valor}'. Debe contener solo números enteros.")
        self.__identificacion = str(valor)

    # ENCAPSULACIÓN Y VALIDACIÓN: NOMBRE
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        # Validación: No puede estar vacío, debe tener al menos 3 caracteres
        if not valor or len(str(valor).strip()) < 3:
            raise ClienteError(f"Nombre inválido: '{valor}'. Debe tener al menos 3 caracteres.")
        self.__nombre = str(valor).strip().title()

    # ENCAPSULACIÓN Y VALIDACIÓN: CORREO
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        # Validación: Uso de expresion recomendada para asegurar formato usuario@dominio.com
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, str(valor)):
            raise ClienteError(f"Correo inválido: '{valor}'. El formato es incorrecto.")
        self.__correo = str(valor).lower()

    # ENCAPSULACIÓN Y VALIDACIÓN: TELÉFONO
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        # Validación: Mínimo 7 números
        if not valor or not str(valor).isdigit() or len(str(valor)) < 7:
            raise ClienteError(f"Teléfono inválido: '{valor}'. Debe tener al menos 7 dígitos numéricos.")
        self.__telefono = str(valor)

    # IMPLEMENTACIÓN DEL MÉTODO ABSTRACTO
    def mostrar_informacion(self):
        return f"Cliente: {self.nombre} | ID: {self.identificacion} | Correo: {self.correo} | Tel: {self.telefono}"



# 4. PRUEBA DE FUNCIONAMIENTO - SIMULACION

if __name__ == "__main__":
    print("--- INICIANDO PRUEBAS DEL MÓDULO DE CLIENTES ---\n")
    
    # Prueba 1: Creación exitosa de un cliente
    try:
        print("Intentando registrar cliente válido...")
        cliente_valido = Cliente(identificacion="1020304050", nombre="Carlos Rodríguez", correo="carlos.r@correo.com", telefono="3001234567")
        print("¡Éxito!", cliente_valido.mostrar_informacion())
    except ClienteError as e:
        print(f"Error detectado: {e}")

    print("-" * 40)

    # Prueba 2: Creación fallida por correo incorrecto
    try:
        print("Intentando registrar cliente con correo inválido...")
        cliente_invalido = Cliente(identificacion="987654321", nombre="Ana Gomez", correo="correo-sin-arroba.com", telefono="3109876543")
        print(cliente_invalido.mostrar_informacion())
    except ClienteError as e:
        print(f"¡Excepción capturada correctamente! -> {e}")
        
    print("-" * 40)
    
    # Prueba 3: Creación fallida por identificación con letras
    try:
        print("Intentando registrar cliente con letras en la identificación...")
        cliente_error_id = Cliente(identificacion="1234ABC", nombre="Luis Perez", correo="luis@correo.com", telefono="3200000000")
    except ClienteError as e:
        print(f"¡Excepción capturada correctamente! -> {e}")