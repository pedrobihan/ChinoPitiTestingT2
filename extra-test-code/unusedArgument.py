def example3(x, y, z):
	a = x + y
	return x + y

def example4(x, y):
	x = y
	return y



# para el  caso adicional example3 demuestra que una variable asignada dentro de la funcion no utilizada,
# no levanta el error, ya que solo se levanta el error de z no utilizada, y no de a, ya que a no
# es un argumento.

# para el caso adicional example4 caso adicional muestra el argumento no usado es redefinido, lo que tampoco
# significa una utilizacion del argumento original