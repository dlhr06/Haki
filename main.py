import argparse
from haki_parser import parse_expression


# Configura el parser de argumentos
parser = argparse.ArgumentParser(description='''
                                 ES: Identifica la información de tu Curriculum Vitae en formato PDF.\n
                                 EN: Identify the information of your Curriculum Vitae in PDF format.\n
                                 FR: Identifiez les informations de votre Curriculum Vitae au format PDF.
                                 ''')
parser.add_argument('command', type=str, help='Comando a ejecutar, por ejemplo: read_pdf. Command to execute, for example: read_pdf. Commande à exécuter, par exemple: read_pdf.')
parser.add_argument('filename', type=str, help='Archivo a procesar')
parser.add_argument('-x', '--from_language', type=str, help='Lenguaje de origen. Source language. Langue source.', default='es')
parser.add_argument('-y','--to_language', type=str, help='Lenguaje de destino. Target language. Langue cible.', default='en')

# Parsea los argumentos de la línea de comandos
args = parser.parse_args()

# Ejecuta la función parse_expression con los argumentos de la línea de comandos
parse_expression(f'{args.command} {args.filename}')