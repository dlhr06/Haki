from lark import Transformer
import yaml

class Evaluator(Transformer):
    def start(self, expression) -> str:
        return expression
    
    def expression(self, commands) -> str:
        return commands
    
    def commands(self, command) -> str:
        return command
    
    def read_pdf(self, filename) -> None:
        filename = filename[0]
        
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
        
        # Guardar el archivo yaml
        try:
            with open(f'{filename.split(".pdf")[0]}_haki.yaml', 'w') as f:
                f.write(yaml_data)
        except Exception as e:
            print(f'Error: {e}')    
    
    def filename(self, tokens) -> str:
        return tokens[0] + "." + tokens[1]