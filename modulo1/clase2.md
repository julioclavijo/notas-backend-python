
Ejercicio 2
Ejercicio de Practica: 
API de Reservas de Hotel (Booking System)
Contexto: Debes crear una API para administrar las reservas de habitaciones de un hotel boutique. Cada reserva tendra un ID Unico autoincremental, el nombre del huésped, el numero de habitacion, el precio por noche y un campo opcional para solicitudes especiales. 

Requerimientos del codigo: 
¢ Base de Datos: Un diccionario global llamado reservas: Dict[int, dict] = {}.
¢ Modelos de Pydantic: 
    o ReservaBase: Con huesped (str), habitacion (int), precio noche (float) y notas (str u opcional).
    o ReservaCrear: Hereda de ReservaBase.
    o ReservaActualizar: Todos los campos anteriores pero opcionales (None), para permitir cambios parciales (ej. si el cliente cambia de habitacion o tarifa).
    o ReservaRespuesta: Hereda de ReservaBase e incluye el id (int).