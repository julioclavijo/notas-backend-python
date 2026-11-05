# Instrucciones del Taller



## Paso 1: Configuración de Variables Globales

Define al inicio de tu script las siguientes constantes del sistema:

* Una clave secreta (`SECRET_KEY`) que consista en una cadena de texto compleja (simulando la clave que solo el servidor backend conoce).
* El algoritmo de firma de tokens (`ALGORITHM`), configurado con el estándar "HS256".



## Paso 2: Construcción del Payload y Tiempo de Expiración

Debes simular que un usuario se ha autenticado con éxito.

1. Utiliza el módulo `datetime` de Python para calcular una fecha y hora exacta en el futuro (15 minutos a partir de ahora). Recuerda trabajar siempre con la zona horaria UTC.
2. Estructura un diccionario (`Payload`) que contenga la información pública del usuario:
* Un ID de usuario numérico.
* Nombre completo.
* Rol del usuario (ej. `"estudiante"` o `"admin"`).
* La fecha de expiración calculada en el subpaso anterior.



> **Nota técnica:** La librería `python-jose` requiere que este valor (`exp`) sea un número entero que represente un Timestamp Unix (puedes usar el método `.timestamp()` y convertirlo a `int`).



## Paso 3: Generación del Token (Encode)

Usa el método apropiado del módulo `jwt` de `python-jose` para codificar e imprimir en la consola el token resultante. Para esto, deberás pasarle como argumentos el payload, la clave secreta y el algoritmo definidos previamente.

* **Resultado esperado:** Deberías ver en consola una cadena larga de texto dividida por dos puntos (`.`), que representan el *Header*, *Payload* y *Signature*.



## Paso 4: Recepción, Validación y Control de Errores (Decode)

Simula que el cliente envía de vuelta ese token para acceder a una ruta protegida. Implementa una estructura de control de excepciones (`try-except`) para procesar el token usando el método de decodificación de la librería:

* **Si el token es válido:** Imprime un mensaje de éxito que extraiga el nombre del usuario directamente desde los datos decodificados.
* **Si el token ha caducado:** Captura específicamente la excepción de expiración de firma (`ExpiredSignatureError`) y muestra un mensaje informando que el token ya no es vigente.
* **Si el token ha sido manipulado:** Captura la excepción general de error de JWT (`JWTError`) y muestra un mensaje indicando que el token es inválido o corrupto.



## Pruebas Obligatorias (Demuestra tu Código)

Una vez que tu script corra perfectamente sin errores, modifica los datos para probar la seguridad del sistema y documenta lo que sucede en la consola:

1. **Prueba de Integridad (El Ataque):** Modifica manualmente un solo carácter de tu variable del token generado justo antes de decodificarlo. ¿Qué error se dispara?
2. **Prueba de Autenticidad (Falsificación):** Intenta decodificar el token original utilizando una clave secreta diferente (ej. `"clave falsa"`). ¿El sistema permite leer los datos?
3. **Prueba de Tiempo (Expiración):** Modifica el cálculo del tiempo en el Paso 2 para que apunte a 5 minutos en el pasado (un token viejo). Ejecuta el script. ¿Tu bloque de excepciones logró atajar el token caducado?