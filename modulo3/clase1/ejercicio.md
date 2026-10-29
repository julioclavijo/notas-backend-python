# Taller: Registro y Login en Consola

## El Reto
Vas a crear un único archivo de Python (por ejemplo, `taller.py`) donde unificarás los dos códigos de clase para implementar un flujo de autenticación continuo.

---

## Instrucciones

### 1. Paso 1: Copiar la base
Copia en tu archivo todas las funciones vistas en clase:
- `hash_password`
- `verify_password`
- `create_token`
- `verify_token`

Incluye también sus importaciones correspondientes:
```python
from jose import jwt
from passlib.context import CryptContext
import os
```

---

### 2. Paso 2: Crear variables globales para simular la Base de Datos
Define estas variables al inicio de tu código para almacenar los datos del usuario:

```python
USUARIO_REGISTRADO = "admin@email.com"
HASH_REGISTRADO = ""  # Inicialmente vacío
```

> **Nota:** Usa precaución al manipular estas variables.

---

### 3. Paso 3: Escribir el flujo principal
Dentro de la función `main()`, implementa la siguiente secuencia utilizando las funciones de clase:

#### a) Simular el Registro
- Asigna a `HASH_REGISTRADO` el hash de una contraseña de tu elección (ejemplo: `"MiClave123"`).
- Imprime el hash generado en consola para confirmar su funcionamiento.

#### b) Simular el Login
- Usa la función `verify_password` para validar la contraseña original contra `HASH_REGISTRADO`.

#### c) Simular la Entrega del Token
- Si la contraseña es correcta, genera un token JWT que contenga:
  - Correo: `"admin@email.com"`
  - Rol: `"administrador"`
- Imprime el token en pantalla.

#### d) Simular el Acceso
- Pasa el token generado a la función `verify_token`.
- Imprime los datos decodificados para verificar que el acceso es válido.

---

## ¿Cómo verificar que tu taller funciona?
Al ejecutar el script, deberías ver en la consola:
1. El texto largo del hash de la contraseña.
2. Un mensaje confirmando que el login fue exitoso.
3. El token JWT (texto largo que comienza con `eyJ...`).
4. Los datos del usuario (correo y rol) impresos al final tras validar el token.

---
## ¡Manos a la obra!
Guarda este enunciado y avísame cuando lo tengas listo o si surge alguna duda durante la implementación del **Paso 3**.