from .rewriter import *

# Clases que permiten transformar codigo que contiene if <expresion> return True else return False 

class SimplifiedIfTransformer(NodeTransformer):

    def visit_Return(self, node):
        if isinstance(node.value, IfExp):
            if isinstance(node.value.body, Constant) and node.value.body.value == True or node.value.body.value == False:
                if isinstance(node.value.orelse, Constant) and node.value.orelse.value != node.value.body.value:
                    if node.value.body.value:
                        return Return(value=node.value.test)
                        
                    else:
                        return Return(value=UnaryOp(op=Not(), operand=node.value.test))
                

class SimplifiedIfRewriterCommand(RewriterCommand):

    def apply(self, ast):
        # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos (e.g., numero de linea) considerando ahora la modificacion
        new_tree = fix_missing_locations(SimplifiedIfTransformer().visit(ast))
        return new_tree
