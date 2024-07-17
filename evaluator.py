from lark import Transformer
import yaml

class Evaluator(Transformer):
    def start(self, expression):
        return expression
    
    def expression(self, commands):
        return commands
    
    def commands(self, command):
        return command
    
    def read_pdf(self, filename):
        # Implementar la lógica para leer el pdf
        
        # Diccionario (ficticio) obtenido del texto del pdf
        cv_data = {
            "personal_information": {
                "name": "Julian",
                "age": 20
            }
        }

        # Convertir el diccionario a formato yaml
        yaml_data = yaml.dump(cv_data,default_flow_style=False, allow_unicode=True)
        
        try:
            with open('cv.yaml', 'w') as f:
                f.write(yaml_data)
            return True 
        except Exception as e:
            print(f'Error: {e}')
            return False
    
    def filename(self, filename):
        return filename
