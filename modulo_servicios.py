from abc import ABC, abstractmethod

# 1. MANEJO DE EXCEPCIONES PERSONALIZADAS

class ServicioError(Exception):
    """Excepción específica para errores en la creación o cálculo de Servicios."""
    pass


# 2. CLASE ABSTRACTA

class Servicio(ABC):
    """Clase abstracta que define el comportamiento base de cualquier servicio."""
    
    def __init__(self, id_servicio, nombre, precio_base):
        if not isinstance(precio_base, (int, float)) or precio_base < 0:
            raise ServicioError(f"El precio base del servicio '{nombre}' debe ser un número positivo.")
        
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.precio_base = precio_base

    # Métodos abstractos que obligan a las clases hijas a implementar su propia lógica
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    # Cumplimiento de "Métodos Sobrecargados" (usando parámetros por defecto en Python)
    # Permite calcular el costo de diferentes formas: con/sin impuesto, con/sin descuento
    def calcular_costo_total(self, impuesto=0.0, descuento=0.0):
        costo_base = self.calcular_costo()
        costo_con_impuesto = costo_base * (1 + impuesto)
        costo_final = costo_con_impuesto - descuento
        
        if costo_final < 0:
            raise ServicioError("El costo final no puede ser negativo después de aplicar el descuento.")
        return round(costo_final, 2)



# 3. CLASES DERIVADAS

# 1 Servicio: Reserva de Salas
class ReservaSala(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, capacidad_personas):
        super().__init__(id_servicio, nombre, precio_base)
        if capacidad_personas <= 0:
            raise ServicioError("La capacidad de la sala debe ser mayor a 0.")
        self.capacidad_personas = capacidad_personas

    def calcular_costo(self):
        # El costo de la sala es fijo, independientemente de las personas
        return self.precio_base

    def describir_servicio(self):
        return f"[Sala] {self.nombre} | Capacidad: {self.capacidad_personas} pax | Precio Fijo: ${self.precio_base}"


# 2 Servicio: Alquiler de Equipos
class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, dias_alquiler):
        super().__init__(id_servicio, nombre, precio_base)
        if dias_alquiler <= 0:
            raise ServicioError("Los días de alquiler deben ser al menos 1.")
        self.dias_alquiler = dias_alquiler

    def calcular_costo(self):
        # El costo depende de la cantidad de días que se alquila
        return self.precio_base * self.dias_alquiler

    def describir_servicio(self):
        return f"[Equipo] {self.nombre} | Días: {self.dias_alquiler} | Total Neto: ${self.calcular_costo()}"


# 3 Servicio: Asesorías Especializadas
class AsesoriaEspecializada(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, horas_asesoria, nivel_experto):
        super().__init__(id_servicio, nombre, precio_base)
        self.horas_asesoria = horas_asesoria
        self.nivel_experto = nivel_experto.lower() # 'junior' o 'senior'

    def calcular_costo(self):
        # El costo se calcula por hora, pero tiene un recargo del 50% si el consultor es Senior
        multiplicador = 1.5 if self.nivel_experto == 'senior' else 1.0
        return (self.precio_base * self.horas_asesoria) * multiplicador

    def describir_servicio(self):
        return f"[Asesoría {self.nivel_experto.title()}] {self.nombre} | Horas: {self.horas_asesoria} | Total Neto: ${self.calcular_costo()}"


# 4. PRUEBA DE FUNCIONAMIENTO (SIMULACIÓN)

if __name__ == "__main__":
    print("--- INICIANDO PRUEBAS DEL MÓDULO DE SERVICIOS ---\n")
    
    try:
        # Polimorfismo: Diferentes servicios calculan sus costos a su manera
        sala = ReservaSala("S01", "Sala de Conferencias", precio_base=150000, capacidad_personas=50)
        equipo = AlquilerEquipo("E01", "Proyector 4K", precio_base=25000, dias_alquiler=3)
        asesoria = AsesoriaEspecializada("A01", "Auditoría de Sistemas", precio_base=80000, horas_asesoria=4, nivel_experto="senior")

        print(sala.describir_servicio())
        print(equipo.describir_servicio())
        print(asesoria.describir_servicio())
        
        print("\n--- PROBANDO MÉTODO 'SOBRECARGADO' (Cálculo con impuestos y descuentos) ---")
        # Aquí usamos el método sobrecargado de la clase padre
        # 1. Sin parámetros extra (Costo neto)
        print(f"Costo neto del Proyector: ${equipo.calcular_costo_total()}")
        
        # 2. Con 19% de IVA
        print(f"Costo del Proyector (+19% IVA): ${equipo.calcular_costo_total(impuesto=0.19)}")
        
        # 3. Con 19% de IVA y un descuento de $10,000
        print(f"Costo del Proyector (+19% IVA - $10k dto): ${equipo.calcular_costo_total(impuesto=0.19, descuento=10000)}")

    except ServicioError as e:
        print(f"Error detectado: {e}")
        
    print("\n--- PROBANDO EXCEPCIONES ---")
    try:
        # Intento de crear una sala con precio negativo para disparar el error
        sala_error = ReservaSala("S02", "Sala VIP", precio_base=-5000, capacidad_personas=10)
    except ServicioError as e:
        print(f"¡Excepción capturada correctamente! -> {e}")