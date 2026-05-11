
# MÓDULO PRINCIPAL DE INTEGRACIÓN
# Curso: Programación 213023 - Universidad Nacional Abierta y a Distancia (UNAD)
# 
# Documentación de Integración de Módulos (Trabajo Colaborativo):
# - Módulo de Clientes  : Clases abstractas, encapsulamiento y validaciones.
# - Módulo de Servicios : Herencia, polimorfismo y parámetros por defecto.
# - Módulo de Reservas  : Vinculación de objetos, control de estado y encadenamiento (Miguel).
# - Módulo de Logs      : Registro persistente en archivo de texto (try/except/finally).
#
# Objetivo: Simulación de 10 operaciones transaccionales demostrando robustez
#           y tolerancia a fallos sin el uso de bases de datos.
# ==============================================================================

from modulo_clientes import Cliente, ClienteError
from modulo_servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada, ServicioError
from modulo_reservas import Reserva, ReservaError, DuracionReservaError
from logger import Logger

def ejecutar_simulacion():
    print("=== INICIANDO SIMULACIÓN DE 10 OPERACIONES (SOFTWARE FJ) ===\n")
    clientes = []
    servicios = []
    reservas = []

    # OPERACIÓN 1: Registro Válido de Cliente

    try:
        print("1. Registrando Cliente Válido 1...")
        c1 = Cliente(identificacion="102030", nombre="Carlos Gomez", correo="carlos@unad.edu.co", telefono="3001112233")
        clientes.append(c1)
        Logger.registrar_evento(f"Éxito: Cliente registrado -> {c1.nombre}")
        print("   -> OK: Cliente creado exitosamente.")
    except Exception as e:
        print(f"   -> Fallo inesperado: {e}")

    # OPERACIÓN 2: Registro Válido de Cliente

    try:
        print("2. Registrando Cliente Válido 2...")
        c2 = Cliente(identificacion="506070", nombre="Ana Martinez", correo="ana@unad.edu.co", telefono="3109998877")
        clientes.append(c2)
        Logger.registrar_evento(f"Éxito: Cliente registrado -> {c2.nombre}")
        print("   -> OK: Cliente creado exitosamente.")
    except Exception as e:
        print(f"   -> Fallo inesperado: {e}")


    # OPERACIÓN 3: Registro Inválido de Cliente (Dispara Excepción)

    try:
        print("3. Intento de Registro Inválido (Correo sin formato)...")
        # El correo intencionalmente no tiene '@' ni dominio para probar tu validación
        c3 = Cliente(identificacion="908070", nombre="Luis Perez", correo="correo_invalido.com", telefono="3201234567")
    except ClienteError as e:
        Logger.registrar_evento(f"Error capturado (Validación Cliente): {e}")
        print(f"   -> Excepción manejada correctamente: {e}")


    # OPERACIÓN 4: Creación Correcta de Servicio (Sala)

    try:
        print("4. Creando Servicio Válido (Reserva de Sala)...")
        s1 = ReservaSala(id_servicio="S01", nombre="Sala de Juntas Principal", precio_base=150000, capacidad_personas=20)
        servicios.append(s1)
        Logger.registrar_evento(f"Éxito: Servicio creado -> {s1.nombre}")
        print("   -> OK: Servicio configurado.")
    except Exception as e:
        print(f"   -> Fallo inesperado: {e}")


    # OPERACIÓN 5: Creación Correcta de Servicio (Equipo)

    try:
        print("5. Creando Servicio Válido (Alquiler de Equipo)...")
        s2 = AlquilerEquipo(id_servicio="E01", nombre="Video Beam 4K", precio_base=30000, dias_alquiler=3)
        servicios.append(s2)
        Logger.registrar_evento(f"Éxito: Servicio creado -> {s2.nombre}")
        print("   -> OK: Servicio configurado.")
    except Exception as e:
        print(f"   -> Fallo inesperado: {e}")


    # OPERACIÓN 6: Creación Incorrecta de Servicio (Dispara Excepción)

    try:
        print("6. Intento de Creación de Servicio Inválido (Precio negativo)...")
        # Pasamos un precio base negativo (-50000) para probar la validación de la clase abstracta
        s3 = AsesoriaEspecializada(id_servicio="A01", nombre="Asesoría de Redes", precio_base=-50000, horas_asesoria=2, nivel_experto="senior")
    except ServicioError as e:
        Logger.registrar_evento(f"Error capturado (Validación Servicio): {e}")
        print(f"   -> Excepción manejada correctamente: {e}")


    # OPERACIÓN 7: Reserva Exitosa (Integración de Objetos)

    try:
        print("7. Generando Reserva Exitosa (Cliente 1 + Sala)...")
        # Vinculamos las instancias de tus módulos usando la clase de Miguel
        r1 = Reserva(codigo_reserva="RES-001", cliente=clientes[0], servicio=servicios[0], duracion=2)
        reservas.append(r1)
        print("   -> OK: Reserva inicializada en estado Pendiente.")
    except Exception as e:
        print(f"   -> Error inesperado en reserva: {e}")


    # OPERACIÓN 8: Reserva Fallida (Duración 0 - Dispara Excepción)

    try:
        print("8. Intento de Reserva con Duración Inválida (0 días)...")
        r2 = Reserva(codigo_reserva="RES-002", cliente=clientes[1], servicio=servicios[1], duracion=0)
    except (ReservaError, DuracionReservaError) as e:
        # Captura la excepción encadenada que programó Miguel
        print(f"   -> Excepción manejada correctamente: {e}")


    # OPERACIÓN 9: Procesamiento de Pago y Confirmación (Polimorfismo)

    try:
        print("9. Procesando Pago de Reserva (Aplicando impuestos y descuentos)...")
        # Ejecuta el cálculo polimórfico y confirma el estado
        total_pagar = reservas[0].procesar_pago(impuesto=0.19, descuento=10000)
        reservas[0].confirmar_reserva()
        print(f"   -> OK: Pago procesado exitosamente. Total: ${total_pagar}")
    except Exception as e:
        print(f"   -> Error procesando transacción: {e}")


    # OPERACIÓN 10: Cancelación de Reserva (Control de Estado)

    try:
        print("10. Ejecutando Cancelación de Reserva...")
        reservas[0].cancelar_reserva()
        # Mostramos el estado final utilizando el método de visualización de Miguel
        info_final = reservas[0].mostrar_reserva().replace("\n", " | ")
        print(f"   -> OK: Estado actualizado.{info_final}")
    except Exception as e:
        print(f"   -> Error en cancelación: {e}")

    print("\n=== SIMULACIÓN FINALIZADA SIN INTERRUPCIONES ===")
    print("Nota: El registro completo de auditoría se encuentra guardado en el archivo de logs del sistema.")

if __name__ == "__main__":
    ejecutar_simulacion()