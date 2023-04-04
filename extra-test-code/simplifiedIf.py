def example3():
	return True if True else False

def example4():
	return False if False else True


# para el caso de example3 se usa el caso de cuando la expresion a retornar es True, de manera que no altera el funcionamiento
# correcto de rewritter en este caso

# para el caso de example4 se usa el caso de cuando la expresion a retornar es False, de manera que no altera el funcionamiento
# correcto de rewritter en este caso aun asi que tenga que hacer not False, se respeta la expresion