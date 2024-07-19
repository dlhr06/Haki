import argparse
from haki_parser import parse_expression

import locale

def main():
    default_locale, _ = locale.getdefaultlocale()
    language = ''
    if default_locale.startswith('es'):
        language = 'es'
    elif default_locale.startswith('fr'):
        language = 'fr'
    else:
        language = 'en'
        
    description = {
        'es': 'Identifica la información de tu Curriculum Vitae en formato PDF.',
        'en': 'Identify the information of your Curriculum Vitae in PDF format.',
        'fr': "Identifiez l'information de votre Curriculum Vitae au format PDF."
    }
    command_help = {
        'es': 'Comando a ejecutar, por ejemplo: read_pdf.',
        'en': 'Command to execute, for example: read_pdf.',
        'fr': 'Commande à exécuter, par exemple: read_pdf.'        
    }
    filename_help = {
        'es': 'Archivo a procesar.',
        'en': 'File to process.',
        'fr': 'Fichier à traiter.'
    }
    from_language_help = {
        'es': 'Lenguaje de origen.',
        'en': 'Source language.',
        'fr': 'Langue source.'
    }
    
    to_language_help = {
        'es': 'Lenguaje de destino.',
        'en': 'Target language.',
        'fr': 'Langue de destination.'
    }
        
    # Configura el parser de argumentos
    parser = argparse.ArgumentParser(description=description.get(language))
    parser.add_argument('command', type=str, help=command_help.get(language))
    parser.add_argument('filename', type=str, help=filename_help.get(language))
    parser.add_argument('-x', '--from_language', type=str, help=from_language_help.get(language), default='es')
    parser.add_argument('-y','--to_language', type=str, help=to_language_help.get(language), default='es')

    # Parsea los argumentos de la línea de comandos
    args = parser.parse_args()

    # Ejecuta la función parse_expression con los argumentos de la línea de comandos
    parse_expression(f'{args.command} {args.filename}')
    
    
    
if __name__ == '__main__':
    main()