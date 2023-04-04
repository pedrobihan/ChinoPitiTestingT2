from .rule import *

# Clases que permiten detectar super innit no llamado

class SuperInitNotCalledVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.call_super = False


    def visit_ClassDef(self, node: ClassDef):

        if node.bases:
            NodeVisitor.generic_visit(self, node)
        
            if not self.call_super:
                self.addWarning('SuperInitNotCalled', node.lineno, 'subclass ' + node.name + ' does not call to super().__init__()')
                
            self.call_super = False

        

    def visit_FunctionDef(self, node: FunctionDef):
        if (node.name  == '__init__'):
            NodeVisitor.generic_visit(self, node)
        
        
    def visit_Call(self, node):
        if isinstance(node.func, Attribute):
            if(node.func.attr == '__init__'):
                if isinstance(node.func.value, Call):
                    if(node.func.value.func.id == 'super'):
                        self.call_super = True



class SuperInitNotCalledRule(Rule):

    def analyze(self, ast):
        visitor = SuperInitNotCalledVisitor()
        visitor.visit(ast)
        return visitor.warningsList()



