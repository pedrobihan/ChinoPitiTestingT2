from .rule import *

# Clases que permiten detectar funciones que tengan un argumento que no se use

class UnusedArgumentVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.arguments = set()
        self.used_arguments = set()

    def visit_Name(self, node: Name):
        if isinstance(node.ctx, Load) and node.id in self.arguments:
            self.used_arguments.add(node.id)
        NodeVisitor.generic_visit(self, node)

    def visit_FunctionDef(self, node: FunctionDef):
        for arg in node.args.args:
            self.arguments.add(arg.arg)
        NodeVisitor.generic_visit(self, node)

        for argument in self.arguments:
            if argument not in self.used_arguments:
                self.addWarning('UnusedArgument', node.lineno, 'argument ' + argument + ' is not used')

        self.used_arguments = set()
        self.arguments = set()


class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        visitor = UnusedArgumentVisitor()
        visitor.visit(ast)
        return visitor.warningsList()



