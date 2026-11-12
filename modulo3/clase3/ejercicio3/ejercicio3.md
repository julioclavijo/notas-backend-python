# Módulo 3 - Clase 3 - Ejercicio 3

## Objetivo
Completar la capa de acceso a datos (`UserRepository`) utilizando SQLAlchemy para implementar las operaciones básicas de un **CRUD** (Create, Read, Update, Delete) sobre el modelo `User`.

---

## Contexto
Actualmente, la clase `UserRepository` ya cuenta con dos métodos implementados que servirán como guía de estilo y manejo de errores:
- **`create`**: Crea un nuevo usuario y maneja conflictos de integridad en la base de datos.
- **`get_by_username`**: Busca un usuario específico por su nombre de usuario.

Tu tarea es implementar los **4 métodos restantes** para completar las operaciones de lectura, actualización y eliminación.

---

## Requerimientos a implementar
Debes agregar los siguientes métodos dentro de la clase `UserRepository` en el archivo `repository/user_repository.py`, respetando estrictamente los nombres de los métodos, parámetros y tipos de retorno indicados:

### 1. Obtener usuario por ID (Read)
- **Firma del método**:
  ```python
  def get_by_id(self, user_id: int) -> User | None:
  ```
- **Comportamiento esperado**:
  Debe consultar la base de datos buscando el usuario cuyo campo `id` coincida con `user_id`.
- **Retorno**:
  El objeto `User` si existe, o `None` en caso contrario.

---

### 2. Listar todos los usuarios (Read)
- **Firma del método**:
  ```python
  def get_all(self, skip: int = 0, limit: int = 100) -> list[User]:
  ```
- **Comportamiento esperado**:
  Debe obtener una lista de usuarios registrados aplicando paginación mediante los parámetros:
  - `skip` (desplazamiento/offset).
  - `limit` (cantidad máxima de registros).
- **Retorno**:
  Una lista de objetos `User` (si no hay registros, devolver una lista vacía `[]`).

---

### 3. Actualizar un usuario (Update)
- **Firma del método**:
  ```python
  def update(self, user_id: int, username: str | None = None, hashed_password: str | None = None) -> User | None:
  ```
- **Comportamiento esperado**:
  1. Buscar si el usuario con `user_id` existe en la base de datos (puedes reutilizar el método `get_by_id`). Si no existe, retornar `None`.
  2. Actualizar **solo los atributos que hayan sido enviados** (es decir, aquellos cuyo valor no sea `None`).
  3. Guardar los cambios en la base de datos. Si ocurre un error de integridad (ej. `IntegrityError` al intentar usar un `username` duplicado), debes:
     - Revertir la transacción (`rollback`).
     - Relanzar la excepción (como se hace en el método `create`).
  4. Refrescar la instancia del usuario antes de devolverla.
- **Retorno**:
  El objeto `User` actualizado, o `None` si el usuario no fue encontrado.

---

### 4. Eliminar un usuario (Delete)
- **Firma del método**:
  ```python
  def delete(self, user_id: int) -> bool:
  ```
- **Comportamiento esperado**:
  1. Buscar si el usuario con `user_id` existe en la base de datos. Si no existe, retornar `False`.
  2. Eliminar el registro de la sesión de base de datos y confirmar la transacción (`commit`).
- **Retorno**:
  `True` si el usuario fue eliminado correctamente, o `False` si el usuario no existía.

---