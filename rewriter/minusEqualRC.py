from .rewriter import *

# Clases que permiten transformar codigo que contiene x = x - y y lo transforma en x -= y
# Considere usar 'literal_eval' para evaluar de manera segura las cadenas que pueden tener expresiones poco confiables. ojo?

class MinusEqualsTransformer(NodeTransformer):

    def visit_Assign(self, node):
        if isinstance(node, Assign):
            if isinstance(node.targets[0], Name):
                if isinstance(node.value, BinOp):
                    if isinstance(node.value.op, Sub):
                        if node.targets[0].id == node.value.left.id:
                            if isinstance(node.value.right, Constant):
                                right_value = node.value.right.value
                                value = Constant(value=right_value)
                            else:
                                right_value = node.value.right.id if isinstance(node.value.right, Name) else None
                                value = Name(id=right_value, ctx=Load())
                            left_value = node.value.left.id if isinstance(node.value.left, Name) else None
                            op = Sub()

                            target = Name(id=left_value, ctx=Store())

                            aug_assign_node = AugAssign(target=target, op=op, value=value)

                            return aug_assign_node
        else:
            return node     
        return  node


class MinusEqualsRewriterCommand(RewriterCommand):
    
    def apply(self, ast):
        # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos (e.g., numero de linea) considerando ahora la modificacion
        new_tree = fix_missing_locations(MinusEqualsTransformer().visit(ast))
        return new_tree