opcional = """
Tarea opcional
Implementar el uso de esta api con la aplicación de TODO's.

Recordar que ya estamos retornando el email del usuario logeado, 
por lo que se tendría que añadir un campo en el modelo TODO, que almacene la 
referencia a la tabla usuario o mediante el email que estamos retornando.

Ejemplo de un campo que puede ser añadido al modelo.

author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
Con el campo añadido y el uso de las rutas, podemos hacer un login para luego
 obtener los TODO's que le corresponden al usuario.

Entonces en base a esa lógica, investigar e implementar la conexión entre TODO's 
y usuarios.

"""