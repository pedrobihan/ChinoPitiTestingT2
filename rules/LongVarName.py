from .rule import *

# Clases que permiten identificar el uso de variables cuyo nombre exede los 15 caracteres
    
class LongVariableNameVisitor(WarningNodeVisitor):
    def visit_Assign(self, node):
        
        if isinstance(node, Assign):
            if isinstance(node.targets[0], Name):
                if len(node.targets[0].id) > 15:
                    self.addWarning('VariableLongName', node.lineno, 'variable '+node.targets[0].id+' has a long name')
            elif isinstance(node.targets[0], Attribute):
                if len(node.targets[0].attr) > 15:
                    self.addWarning('VariableLongName', node.lineno, 'variable '+node.targets[0].attr+' has a long name') # aca node debe ser el nombre de la var

class LongVariableNameRule(Rule):
    def analyze(self, ast):
        visitor = LongVariableNameVisitor()
        visitor.visit(ast)
        return visitor.warningsList()