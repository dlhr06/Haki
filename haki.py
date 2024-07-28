import asyncio
import argparse
import locale
import tracemalloc

from haki_parser import parse_expression
from language_dictionary import (description, commands, command_read_pdf, command_get_professional_summary,
                                command_get_motivation_letter, command_apply_for_job, 
                                arg_pdf_filename, arg_yaml_filename, arg_url, arg_credentials
                                )
from evaluator import Evaluator

async def main():
    default_locale, _ = locale.getlocale()
    language = ''
    if default_locale.startswith('es'):
        language = 'es'
    elif default_locale.startswith('fr'):
        language = 'fr'
    else:
        language = 'en'
        
    # Configura el parser de argumentos
    parser = argparse.ArgumentParser(description=description.get(language), formatter_class=argparse.ArgumentDefaultsHelpFormatter, epilog='Haki v0.1.0' )

    # Definir subparsers para cada comando
    subparsers = parser.add_subparsers(dest='command', help=commands.get(language))
    
    # Comando read_pdf
    parser_read_pdf = subparsers.add_parser('read_pdf', help=command_read_pdf.get(language))
    parser_read_pdf.add_argument('filename', type=str, help=arg_pdf_filename.get(language))

    
    # Comando get_professional_summary
    parser_get_professional_summary = subparsers.add_parser('get_professional_summary', help=command_get_professional_summary.get(language))
    parser_get_professional_summary.add_argument('filename', type=str, help=arg_yaml_filename.get(language))

    # Comando get_motivation_letter
    parser_get_motivation_letter = subparsers.add_parser('get_motivation_letter', help=command_get_motivation_letter.get(language))
    parser_get_motivation_letter.add_argument('filename', type=str, help=arg_yaml_filename.get(language))

    # Comando apply_for_job
    parser_apply_for_job = subparsers.add_parser('apply_for_job', help=command_apply_for_job.get(language))
    parser_apply_for_job.add_argument('filename_yaml', type=str, help=arg_yaml_filename.get(language))
    parser_apply_for_job.add_argument('filename_pdf', type=str, help=arg_pdf_filename.get(language))
    parser_apply_for_job.add_argument('url', type=str, help=arg_url.get(language))
    parser_apply_for_job.add_argument('credentials', type=str, help=arg_credentials.get(language))

    # Parsea los argumentos de la línea de comandos
    args = parser.parse_args()
        
    if args.command == 'apply_for_job':        
        await parse_expression(f'{args.command} {args.filename_yaml} {args.filename_pdf} {args.url} {args.credentials}')[0][0][0]
    else:
        parse_expression(f'{args.command} {args.filename}')
    
if __name__ == '__main__':
    tracemalloc.start()
    # main()
    asyncio.run(main())