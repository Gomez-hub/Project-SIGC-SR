from modulo_clientes import Cliente, ClienteError

from modulo_servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada,
    ServicioError
)

from modulo_reservas import (
    Reserva,
    ReservaError
)

from logger import Logger


print("\n========== SISTEMA SOFTWARE FJ ==========\n")


# OPERACIÓN 1
try:

    cliente1 = Cliente(
        "102030",
        "Miguel Gomez",
        "miguel@gmail.com",
        "3001234567"
    )


    print(cliente1.mostrar_informacion())


except ClienteError as e:

    print(e)


# OPERACIÓN 2

try:

    cliente3 = Cliente(
        "ABC123",
        "Ana",
        "correo-mal",
        "123"
    )

except ClienteError as e:

    print(f"ERROR CLIENTE: {e}")


# OPERACIÓN 3
try:

    sala = ReservaSala(
        "S01",
        "Sala Conferencias",
        200000,
        50
    )

    print(sala.describir_servicio())

except ServicioError as e:

    print(e)


# OPERACIÓN 4
try:

    equipo = AlquilerEquipo(
        "E01",
        "Proyector",
        30000,
        3
    )

    print(equipo.describir_servicio())

except ServicioError as e:

    print(e)


# OPERACIÓN 5
try:

    asesoria = AsesoriaEspecializada(
        "A01",
        "Consultoría Python",
        100000,
        5,
        "senior"
    )

    print(asesoria.describir_servicio())

except ServicioError as e:

    print(e)


# OPERACIÓN 6
try:

    reserva1 = Reserva(
        "R001",
        cliente1,
        sala,
        2
    )

    reserva1.confirmar_reserva()

    print(reserva1.mostrar_reserva())

except ReservaError as e:

    print(e)


# OPERACIÓN 7
try:

    total = reserva1.procesar_pago(
        impuesto=0.19,
        descuento=10000
    )

    print(f"\nTOTAL PAGADO: ${total}")

except ReservaError as e:

    print(e)


# OPERACIÓN 8
try:

    reserva2 = Reserva(
        "R002",
        cliente1,
        equipo,
        -5
    )

except ReservaError as e:

    print(f"ERROR RESERVA: {e}")


# OPERACIÓN 9
try:

    servicio_error = ReservaSala(
        "S02",
        "Sala VIP",
        -5000,
        10
    )

except ServicioError as e:

    print(f"ERROR SERVICIO: {e}")


# OPERACIÓN 10
try:

    reserva1.cancelar_reserva()

    print(
        f"\nEstado actual reserva: {reserva1.estado}"
    )

except Exception as e:

    print(e)


finally:

    print("\nSistema ejecutado correctamente.")