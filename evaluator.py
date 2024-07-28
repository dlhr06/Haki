from lark import Transformer,v_args
import yaml
import os
from classified_llm import generate_dictionary

from semantic import file_exists

class Evaluator(Transformer):
    def start(self, expression:str) -> str:
        return expression
    
    def expression(self, commands:str) -> str:
        return commands
    
    def commands(self, command:str) -> str:
        return command
    
    def read_pdf(self, filename:str=None) -> None:
        if not filename[0]:
            return False
        
        print(f'Función read_pdf: {filename}')
        filename = filename[0]
        print(f'filename: {filename}')

        cv_dictionary = generate_dictionary(str(filename))
        
        '''cv_dictionary = generate_dictionary(filename)

        # Convertir el diccionario a formato yaml
        yaml_data = yaml.dump(cv_dictionary,default_flow_style=False, allow_unicode=True)
        
        # Obtener el directorio actual de trabajo
        current_dir = os.getcwd()
        
        # Crear la ruta completa del archivo yaml
        yaml_filename = os.path.join(current_dir, f'{filename.split(".pdf")[0]}_haki.yaml')

        # Guardar el archivo yaml
        try:
            with open(yaml_filename, 'w') as f:
                f.write(yaml_data)
            print(f'YAML file created in: {yaml_filename}')
        #except Exception as e:
            #print(f'Error: {e}')    
        '''
    def get_professional_summary(self, filename:str) -> None:
        print(f'Función get_professional_summary: {filename}')
        # Implementar la lógica para generar un resumen profesional
        pass
    
    def get_motivation_letter(self, filename:str) -> None:
        print(f'Función get_motivation_letter: {filename}')
        # Implementar la lógica para generar una carta de motivación
        pass
    
    @v_args(inline=True)
    def apply_for_job(self, filename:str, route:str) -> None:
        print(f'''
            Función apply_for_job: 
            filename: {filename}
            url: {route}
            ''')
        # Implementar la lógica para aplicar a una oferta de trabajo
        pass
    
    def filename_pdf(self, filename) -> str|bool:
        if file_exists(filename[0]):
            return filename[0]
        print(f'Error: El archivo {filename[0]} no existe.')
        return False
    
    def filename_yaml(self, filename) -> str|bool:
        print(f'filename_yaml: {filename[0]}')
        if file_exists(filename[0]):
            return filename[0]
        print(f'Error: El archivo {filename[0]} no existe.')
        return False
    
    def route(self, url) -> str:
        print(f'URL: {url[0]}')
        return url[0]
    