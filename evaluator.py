from lark import Transformer

class Evaluator(Transformer):
    def start(self, expression):
        return expression
    
    def expression(self, commands):
        return commands
    
    def commands(self, command):
        return command
    
    def read_pdf(self, filename):
        # Implementar la lógica para leer el PDF
        return f"Reading PDF: {filename}"
    
    def filename(self, name, extension):
        return name + '.' + extension
