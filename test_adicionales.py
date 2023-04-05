import unittest
from rules import *
from rewriter import *

"""
Template para los tests de las reglas y transformaciones adicionales propuestos por usted.
IMPORTANTE: 
    - Deben existir al menos 5 tests, uno por cada regla/transformador implementado.
    - Los codigos a ser analizados usados en los tests deben ser diferentes.
    - Los tests adicionales deben ser diferentes a los del archivo tests-tarea.py
    - Si usted implemento la tarea en un nuevo archivo dentro del folder rules o rewriter
    no olvide modificar el __init__.py de rules y rewriter para importar los archivos necesarios para su tarea.
    Caso contrario importe lo necesario en este archivo.
"""

class TestWarnings(unittest.TestCase):


    # Funcion que recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree

    """ Nombre: test_long_variable_name
        Codigo a ser analizado: extra-test-code/longVariableName.py
        Descripcion: Test para evaluar LongVariableNameRule considerando los siguientes escenarios:
        - Linea 2 : asignación de valor a una variable - no se deberría poder dado que variables muy largas entorpecen el código.
        - Linea 4 : operación sobre una variable de nombre largo - no debería arrojar error dado que no usa el método Assign id, 
                                                                   solo asigna cambio de valor a variable que ya fue identificada como erronea.
        - Linea 9 : se asigna atributo a variable en una  función de una clase - se usa método Assign y su id queda muy largo (se cuentan los 
                                                                5 caracteres de "self." mas los que tenga el nombre de la variable).
        - Linea 12 : se asigna atributo a variable en una  función de una clase - se usa método Assign y su id queda muy largo (se cuentan los 
                                                                5 caracteres de "self." mas los que tenga el nombre de la variable).

        Resultado esperado: [Warning('VariableLongName', 2, 'variable contadorsuperlargooficial has a long name'),
                            Warning('VariableLongName', 9, 'variable nombrevariablemuylargolarguisimo has a long name'),
                            Warning('VariableLongName', 12, 'variable nombrevariablemuylargolarguisimo has a long name')]
    """

    def test_long_variable_name(self):
        tree = self.get_ast_from_file('extra-test-code/longVariableName.py')

        longNameRule = LongVariableNameRule()
        result = longNameRule.analyze(tree)


        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [Warning('VariableLongName', 2, 'variable contadorsuperlargooficial has a long name'),
                            Warning('VariableLongName', 9, 'variable nombrevariablemuylargolarguisimo has a long name'),
                            Warning('VariableLongName', 12, 'variable nombrevariablemuylargolarguisimo has a long name')]

        self.assertEqual(result, expectedWarnings)

    """ Nombre: test_unused_argument
        Codigo a ser analizado: extra-test-code/unusedArgument.py
        Descripcion: Test para evaluar UnusedArgumentRule considerando los siguientes escenarios:
        - Linea <numero-linea> : <Descripcion de codigo - caso a considerar>
        
        Resultado esperado (Una lista de warnings): .....
    """

    def test_unused_argument(self):
        tree = self.get_ast_from_file('extra-test-code/unusedArgument.py')

        unusedArgRule = UnusedArgumentRule()
        result = unusedArgRule.analyze(tree)

        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [Warning('UnusedArgument', 1, 'argument z is not used'),
                            Warning('UnusedArgument', 5, 'argument y is not used'),
                            Warning('UnusedArgument', 5, 'argument z is not used')]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_super_init_not_called
        Codigo a ser analizado: extra-test-code/superInitNotCalled.py
        Descripcion: Test para evaluar SuperInitNotCalledRule considerando los siguientes escenarios:
        - Linea <numero-linea> : <Descripcion de codigo - caso a considerar>
        
        Resultado esperado (Una lista de warnings): .....
    """

    def test_super_init_not_called(self):
        tree = self.get_ast_from_file('extra-test-code/superInitNotCalled.py')

        superInitRule = SuperInitNotCalledRule()
        result = superInitRule.analyze(tree)

        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [Warning('SuperInitNotCalled', 13, 'subclass Child2 does not call to super().__init__()')]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_minus_equal_rewriter
        Codigo a ser analizado: extra-test-code/minusEquals.py
        Descripcion: Test para evaluar transformador MinusEqualsRewriterCommand considerando los siguientes escenarios:
        - Linea 2 : test para evaluar la substraccion de dos caracteres, donde ninguno de esos es la variable a asignar -
        lo anterior considera un caso que fue borde al crear la función, donde x = y - z, con x != y, si no se agregaba ese 
        caso borde, x = y - z hubiese sido reemplazado por x -= z, lo cual era incorrecto 
        
        Resultado esperado: extra-test-code/expectedMinusEquals.py
    """

    def test_minus_equal_rewriter(self):
        tree = self.get_ast_from_file('extra-test-code/minusEquals.py')

        command = MinusEqualsRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('extra-test-code/expectedMinusEquals.py')

        self.assertEqual(dump(tree), dump(expectedCode))


    """ Nombre: test_simplified_if
        Codigo a ser analizado: extra-test-code/simplifiedIf.py
        Descripcion: Test para evaluar SimplifiedIfRewriterCommand considerando los siguientes escenarios:
        - Linea <numero-linea> : <Descripcion de codigo - caso a considerar>
        
        Resultado esperado: extra-test-code/expectedSimplifiedIf.py
    """

    def test_simplified_if(self):
        tree = self.get_ast_from_file('extra-test-code/simplifiedIf.py')

        command = SimplifiedIfRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('extra-test-code/expectedSimplifiedIf.py')
        
        self.assertEqual(dump(tree), dump(expectedCode))

if __name__ == '__main__':
    unittest.main()
