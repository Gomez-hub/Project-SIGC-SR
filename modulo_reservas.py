from modulo_clientes import ClienteError
from modulo_servicios import ServicioError

from logger import Logger


# EXCEPCIONES PERSONALIZADAS

class ReservaError(Exception):
    """Excepción general para errores en reservas"""
    pass


class DuracionReservaError(ReservaError):
    """Error cuando la duración es inválida"""
    pass


# CLASE RESERVA

class Reserva:

    def __init__(self, codigo_reserva, cliente, servicio, duracion):

        try:

            if duracion <= 0:
                raise DuracionReservaError(
                    "La duración de la reserva debe ser mayor a 0"
                )

            self.codigo_reserva = codigo_reserva
            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "Pendiente"

            Logger.registrar_evento(
                f"Reserva creada: {codigo_reserva}"
            )

        except Exception as e:

            Logger.registrar_evento(
                f"ERROR creando reserva: {e}"
            )

            raise ReservaError(
                "No fue posible crear la reserva"
            ) from e

    # CONFIRMAR RESERVA
    def confirmar_reserva(self):

        try:

            self.estado = "Confirmada"

            Logger.registrar_evento(
                f"Reserva confirmada: {self.codigo_reserva}"
            )

        except Exception as e:

            Logger.registrar_evento(
                f"ERROR confirmando reserva: {e}"
            )

    # CANCELAR RESERVA
    def cancelar_reserva(self):

        try:

            self.estado = "Cancelada"

            Logger.registrar_evento(
                f"Reserva cancelada: {self.codigo_reserva}"
            )

        except Exception as e:

            Logger.registrar_evento(
                f"ERROR cancelando reserva: {e}"
            )

    # PROCESAR PAGO
    def procesar_pago(self, impuesto=0.0, descuento=0.0):

        try:

            total = self.servicio.calcular_costo_total(
                impuesto,
                descuento
            )

            Logger.registrar_evento(
                f"Pago procesado reserva {self.codigo_reserva}: ${total}"
            )

            return total

        except ServicioError as e:

            Logger.registrar_evento(
                f"ERROR procesando pago: {e}"
            )

            raise ReservaError(
                "No se pudo procesar el pago"
            ) from e

    # MOSTRAR INFORMACIÓN
    def mostrar_reserva(self):

        return (
            f"\nReserva: {self.codigo_reserva}"
            f"\nCliente: {self.cliente.nombre}"
            f"\nServicio: {self.servicio.nombre}"
            f"\nDuración: {self.duracion}"
            f"\nEstado: {self.estado}"
        )