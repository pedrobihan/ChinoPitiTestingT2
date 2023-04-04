class Parent:

	def __init__(self, name):
		self.name = name


class Child1(Parent):

	def __init__(self, name):
		super(self).__init__(name)


class Child2(Parent):

	def __init__(self, name):
		self.name = name

	def superMalo(self):
		super(self).__init__()


# para el  caso adicional Child1 demuestra que una sintaxis distinta para llamar super().__init__() no levanta
# error, lo que es correcto

# para el caso adicional Child2 caso adicional muestra el error cuando ocurre un llamado a super() pero no en la 
# funcion __init__ de la subclase, mostrando un caso de error adicional